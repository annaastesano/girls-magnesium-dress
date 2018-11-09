import logging
import os
import pytz

from core.models import Survey, SurveyResult
from core.qualtrics import benchmark, download, exceptions, question
from django.conf import settings

from google.appengine.api import mail
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.shortcuts import reverse
from django.template.loader import get_template
from django.db import IntegrityError
from djangae.db import transaction
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
import cloudstorage
from google.appengine.api import app_identity
import csv
from datetime import datetime
import json


def get_results():
    """Download survey results from Qualtrics.
    The function will use the latest stored `response_id` if any, otherwise
    download all the available results from Qualtrics.
    """
    try:
        survey_result = SurveyResult.objects.latest('started_at')
        started_after = survey_result.started_at
        logging.info('Some Survey results has already been downloaded, partially download new results.')
    except SurveyResult.DoesNotExist:
        started_after = None
        logging.info('No Survey results has already been downloaded so far, download all the results.')

    try:
        results = download.fetch_results(started_after=started_after)
        responses = results.get('responses')
        new_response_ids = _create_survey_results(responses)
        to_key, bcc_key = settings.QUALTRICS_EMAIL_TO, settings.QUALTRICS_EMAIL_BCC
        email_list = [(item.get(to_key), item.get(bcc_key), item.get('sid')) for item in responses
                      if _survey_completed(item.get('Finished')) and item.get('ResponseID') in new_response_ids]
        if email_list:
            send_emails_for_new_reports(email_list)
    except exceptions.FetchResultException as fe:
        logging.error('Fetching results failed with: {}'.format(fe))


def _create_survey_results(results_data):
    """Create `SurveyResult` given a list of `result_data`.

    :param results_data: dictionary containing the downloaded responses
        from Qualtrics API.

    :returns: list of `response_id` for each `core.SurveyResult` created.
    """
    response_ids = []
    for data in results_data:
        try:
            new_survey_result = _create_survey_result(data)
            if new_survey_result:
                response_ids.append(new_survey_result)
        except exceptions.InvalidResponseData as e:
            logging.error(e)
    return response_ids


def _create_survey_result(data):
    """Create `SurveyResult` given a single `result_data`.

    :param data: dictionary of data downloaded from Qualtrics
    :returns: `response_id` if a `core.SurveyResult` is created, None
        otherwise.
    """
    if not _survey_completed(data.get('Finished')):
        logging.warning('Found unfinshed survey {}: SKIP'.format(data.get('sid')))
        return

    response_id = data['ResponseID']
    new_survey_result = None
    try:
        with transaction.atomic(xg=True):
            questions = question.data_to_questions(data)
            dmb, dmb_d = benchmark.calculate_response_benchmark(questions)
            excluded_from_best_practice = question.discard_scores(data)
            survey_result = SurveyResult.objects.create(
                survey_id=data.get('sid'),
                response_id=response_id,
                started_at=make_aware(parse_datetime(data.get('StartDate')), pytz.timezone('US/Mountain')),
                excluded_from_best_practice=excluded_from_best_practice,
                dmb=dmb,
                dmb_d=dmb_d,
            )
            new_survey_result = response_id
            try:
                s = Survey.objects.get(pk=data.get('sid'))
                s.last_survey_result = survey_result
                s.save()
            except Survey.DoesNotExist:
                logging.warning('Could not update Survey with sid {}'.format(data.get('sid')))
    except IntegrityError:
        logging.info('SurveyResult with response_id: {} has already been saved.'.format(response_id))
    return new_survey_result


def send_emails_for_new_reports(email_list):
    """Send an email for every element of `email_list`.

    :param email_list: tuple of element (to, bcc, sid)
    """
    domain = os.environ['HTTP_HOST']
    subject_template = get_template("core/response_ready_email_subject.txt")
    html_message_template = get_template("core/response_ready_email_body.html")
    text_message_template = get_template("core/response_ready_email_body.txt")

    for email_data in email_list:
        to, bcc, sid = email_data

        # Last minute change, we should refactor this and pass the object in
        try:
            s = Survey.objects.get(pk=sid)
            company_name = s.company_name
            industry = s.get_industry_display()
            country = s.get_country_display()
        except Survey.DoesNotExist:
            company_name = ""
            industry = ""
            country = ""
            logging.warning('Could not find Survey with sid {} to get context string for email'.format(sid))

        if is_valid_email(to):
            link = reverse('report', kwargs={'sid': sid})
            bcc = [bcc] if is_valid_email(bcc) else None
            context = {
                'url': "http://{}{}".format(domain, link),
                'company_name': company_name,
                'industry': industry,
                'country': country,
            }

            email_kwargs = {
                'to': [to],
                'subject': subject_template.render(context).split("\n")[0],
                'sender': settings.CONTACT_EMAIL,
                'body': text_message_template.render(context),
                'html': html_message_template.render(context),
            }

            if getattr(settings, 'REPLY_TO_EMAIL', None):
                email_kwargs['reply_to'] = settings.REPLY_TO_EMAIL

            message = mail.EmailMessage(**email_kwargs)

            if bcc:
                message.bcc = bcc

            message.send()

            logging.info("Email sent to {} from {} for Survey with sid={}".format(to, settings.CONTACT_EMAIL, sid))


def is_valid_email(email):
    email_validator = EmailValidator()
    try:
        email_validator(email)
    except ValidationError:
        return False
    return True


def _survey_completed(is_finished):
    is_finished = int(is_finished)
    return bool(is_finished)


def generate_csv_export(created_at=None):
    surveys = Survey.objects.none()
    if created_at:
        surveys = Survey.objects.all()
    else:
        # surveys = Survey.objects.filter(created_at__gte=datetime)
        pass

    bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    bucket = '/' + bucket_name
    filename = os.path.join(bucket, 'export-{}.csv'.format(datetime.now().strftime('%Y%m%d-%H%M%S')))

    logging.info("Creating export in {}".format(filename))

    write_retry_params = cloudstorage.RetryParams(backoff_factor=1.1)
    with cloudstorage.open(filename, 'w', content_type='text/csv', retry_params=write_retry_params) as gcs_file:
        fieldnames = [
            'company_name',
            'industry',
            'dmb_d',
            'access',
            'audience',
            'attribution',
            'ads',
            'organization',
            'automation',
        ]
        writer = csv.writer(gcs_file, delimiter=',')
        writer = csv.DictWriter(gcs_file, fieldnames=fieldnames)
        writer.writeheader()

        for survey in surveys:
            survey_data = {
                'company_name': survey.company_name,
                'industry': survey.industry,
                'country': survey.country,
                'dmb': survey.last_survey_result.dmb if survey.last_survey_result else None,
                'access': None,
                'audience': None,
                'attribution': None,
                'ads': None,
                'organization': None,
                'automation': None,
            }

            if survey.last_survey_result_data:
                survey_data.update(json.loads(survey.last_survey_result_data.dmb_d))

            writer.writerow(survey_data)
    logging.info("Export completed")
