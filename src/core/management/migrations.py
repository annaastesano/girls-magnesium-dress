from django.conf import settings

from core.models import Survey, SurveyResult
import logging
from core.googleapi import sheets

import unicodecsv as csv
from core.management.dmb_lite import csv_string
from core.models import User, Survey
from os.path import join


CSV_PATH = join(settings.BASE_DIR, "core/management/tests/csv_mock_dmblite.csv")

# INDUSTRY_MAP = {
#     'Automotive': 'ma-v',
#     'Retail': 'rt-o',
#     'Healthcare': 'ic-o',
#     'Education & Government': 'edu-o',
#     'Technology': 'ic-o',
#     'Services All Verticals': 'other',
#     'Finance': 'fi-o',
#     'Consumer Packaged Goods':
#     Classifieds & Local
#     Business & Industrial Markets
#     Travel
#     Media & Entertainment
# }

def migrate_to_dmblite_survey():
    # Enable all tenants since the Survey.save method will
    # error if a Survey is using a disabled tenant
    logging.info("Enabling cloud tenant")
    settings.ALL_TENANTS['cloud']['enabled'] = True
    settings.TENANTS = {k: v for k, v in settings.ALL_TENANTS.items() if v['enabled']}

    logging.info("Adding DMBLite fields to surveys")
    surveys = Survey.objects.all()
    logging.info("Found {} surveys to be converted".format(surveys.count()))
    for survey in surveys:
        try:
            survey.save()
        except AssertionError:
            logging.error("Something went wrong migrating survey {} ".format(survey.sid))

    for survey_result in SurveyResult.objects.all():
        survey_result.save()
    # Disable all tenants after task
    logging.info("Disabling cloud tenant")
    settings.ALL_TENANTS['cloud']['enabled'] = False
    settings.TENANTS = {k: v for k, v in settings.ALL_TENANTS.items() if v['enabled']}


def resave_surveys():
    for s in Survey.objects.all():
        try:
            s.save()
        except AssertionError:
            logging.error("Could not save {} ".format(s.sid))


def drop_search_index():
    from google.appengine.api import search
    for index in search.get_indexes(fetch_schema=True):
        logging.info("index %s", index.name)
        logging.info("schema: %s", index.schema)
        document_ids = [
            document.doc_id
            for document
            in index.get_range(ids_only=True)]
        index.delete(document_ids)
        index.delete_schema()


def import_dmb_lite():
    print(CSV_PATH)
    csvfile = open(CSV_PATH, 'r')
    reader = csv.reader(csvfile, delimiter=",")


    for i, row in enumerate(reader):
        if i > 3:

            ldap = row[8]
            company_name = row[2]
            industry = 'other' # need to wait for mapping
            country = row[9]
            user = create_user_(ldap)
            tenant = "ads"
            account_id = row[3] if row[3] != 'undefined' else row[4]
            user = create_user_(ldap)

            existing_accounts = Survey.objects.filter(company_name=company_name, account_id=account_id, country=country)

            if existing_accounts.count() == 0:
                s = Survey(company_name=company_name, industry=industry, country=country, tenant=tenant, account_id=account_id, creator=user)
                s.save()
            else:
                s = existing_accounts[0]

            if not user.accounts.filter(pk=s.pk).exists():
                user.accounts.add(s)
                user.save()



def create_user_(ldap):
    email = '{}@google.com'.format(ldap.lower())
    user, _ = User.objects.get_or_create(email_lower=email, defaults={"email": email})

    return user
