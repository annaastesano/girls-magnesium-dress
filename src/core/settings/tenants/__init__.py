# flake8: noqa
#####  GOOGLE SHEETS EXPORT FOR TENANTS #####
GOOGLE_SHEET_BASE_SURVEY_FIELDS = {
    'company_name': 'Company Name',
    'account_id': 'Account ID',
    'country': 'Country',
    'industry': 'Industry',
    'created_at': 'Creation Date',
    'link': 'Survey link',
}

GOOGLE_SHEET_BASE_RESULT_FIELDS = {
    'dmb': 'Overall DMB',
    'excluded_from_best_practice': 'Excluded from Benchmark',
    'absolute_report_link': 'Report link',
    'absolute_detail_link': 'Detail link',
}

GOOGLE_SHEET_SURVEY_CHOICE_FIELDS = ('industry', 'country',)
#####  END OF GOOGLE SHEETS EXPORT FOR TENANTS #####


import ads as advertisers_conf
import news as news_conf
import retail as retail_conf
import cloud as cloud_conf
from djangae.environment import application_id
from django.utils.translation import gettext_lazy as _


ADS = 'ads'
NEWS = 'news'
RETAIL = 'retail'
CLOUD = 'cloud'


ALL_TENANTS = {
    ADS: {
        'key': ADS,
        'label': _('Advertisers'),
        'slug': 'advertisers',
        'in_dmb_footer': True,
        'footer_label': _('Advertiser Marketing Maturity'),
        'QUALTRICS_SURVEY_ID': 'SV_6igS0eu8kjbqV5H',
        'EMAIL_TO': 'Q97_4_TEXT',
        'EMAIL_BCC': 'Q97_5_TEXT',
        'DIMENSIONS': advertisers_conf.DIMENSIONS,
        'HIERARCHICAL_INDUSTRIES': advertisers_conf.HIERARCHICAL_INDUSTRIES,
        'INDUSTRIES': advertisers_conf.INDUSTRIES,
        'CONTENT_DATA': advertisers_conf.CONTENT_DATA,
        'MULTI_ANSWER_QUESTIONS': advertisers_conf.MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': advertisers_conf.WEIGHTS,
        'EXCLUDED_TIME_THRESHOLD': 5,
        'CONTACT_EMAIL': "Digital Maturity Benchmark <no-reply@{}.appspotmail.com>".format(application_id()),
        'i18n': True,
        'GOOGLE_SHEET_EXPORT_SURVEY_FIELDS': advertisers_conf.GOOGLE_SHEET_EXPORT_SURVEY_FIELDS,
        'GOOGLE_SHEET_EXPORT_RESULT_FIELDS': advertisers_conf.GOOGLE_SHEET_EXPORT_RESULT_FIELDS,
        'PRODUCT_NAME': "Digital Maturity Benchmark",
        'enabled': True,
    },
    NEWS: {
        'key': NEWS,
        'label': _('News'),
        'slug': 'news',
        'in_dmb_footer': True,
        'footer_label': _('News Publisher Data Transformation'),
        'QUALTRICS_SURVEY_ID': 'SV_4JxgntrYg5uiMyp',
        'EMAIL_TO': 'Q1_4_TEXT',
        'EMAIL_BCC': 'Q1_5_TEXT',
        'DIMENSIONS': news_conf.DIMENSIONS,
        'HIERARCHICAL_INDUSTRIES': news_conf.HIERARCHICAL_INDUSTRIES,
        'INDUSTRIES': news_conf.INDUSTRIES,
        'CONTENT_DATA': news_conf.CONTENT_DATA,
        'MULTI_ANSWER_QUESTIONS': news_conf.MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': news_conf.WEIGHTS,
        'DIMENSIONS_WEIGHTS_QUESTION_ID': news_conf.DIMENSIONS_WEIGHTS_QUESTION_ID,
        'DIMENSIONS_WEIGHTS': news_conf.DIMENSIONS_WEIGHTS,
        'FORCED_INDUSTRY': 'ic-bnpj',
        'EXCLUDED_TIME_THRESHOLD': 2,
        'CONTACT_EMAIL': "Data Maturity Benchmark <no-reply@{}.appspotmail.com>".format(application_id()),
        'i18n': False,
        'GOOGLE_SHEET_EXPORT_SURVEY_FIELDS': news_conf.GOOGLE_SHEET_EXPORT_SURVEY_FIELDS,
        'GOOGLE_SHEET_EXPORT_RESULT_FIELDS': news_conf.GOOGLE_SHEET_EXPORT_RESULT_FIELDS,
        'PRODUCT_NAME': "Data Maturity Benchmark",
        'enabled': True,
    },
    RETAIL: {
        'key': RETAIL,
        'label': _('Retail'),
        'slug': 'retaildatatransformation',
        'in_dmb_footer': True,
        'footer_label': _('Retail Data Transformation'),
        'QUALTRICS_SURVEY_ID': 'SV_b1OV8m7xVD337rD',
        'EMAIL_TO': 'Q1_4_TEXT',
        'EMAIL_BCC': 'Q1_5_TEXT',
        'DIMENSIONS': retail_conf.DIMENSIONS,
        'HIERARCHICAL_INDUSTRIES': retail_conf.HIERARCHICAL_INDUSTRIES,
        'INDUSTRIES': retail_conf.INDUSTRIES,
        'CONTENT_DATA': retail_conf.CONTENT_DATA,
        'MULTI_ANSWER_QUESTIONS': retail_conf.MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': retail_conf.WEIGHTS,
        'DIMENSIONS_WEIGHTS_QUESTION_ID': retail_conf.DIMENSIONS_WEIGHTS_QUESTION_ID,
        'DIMENSIONS_WEIGHTS': retail_conf.DIMENSIONS_WEIGHTS,
        'FORCED_INDUSTRY': 'rt-o',
        'EXCLUDED_TIME_THRESHOLD': 2,
        'CONTACT_EMAIL': "Data Maturity Benchmark <no-reply@{}.appspotmail.com>".format(application_id()),
        'i18n': False,
        'GOOGLE_SHEET_EXPORT_SURVEY_FIELDS': retail_conf.GOOGLE_SHEET_EXPORT_SURVEY_FIELDS,
        'GOOGLE_SHEET_EXPORT_RESULT_FIELDS': retail_conf.GOOGLE_SHEET_EXPORT_RESULT_FIELDS,
        'PRODUCT_NAME': "Data Maturity Benchmark",
        'enabled': True,
    },
    CLOUD: {
        'key': CLOUD,
        'label': _('Cloud'),
        'slug': 'cloud',
        'in_dmb_footer': False,
        'footer_label': _('Cloud Maturity Benchmark'),
        'QUALTRICS_SURVEY_ID': 'SV_eRioRXZ4UcKYpVj',
        'EMAIL_TO': 'Q3_4_TEXT',
        'EMAIL_BCC': 'Q3_5_TEXT',
        'DIMENSIONS': cloud_conf.DIMENSIONS,
        'HIERARCHICAL_INDUSTRIES': cloud_conf.HIERARCHICAL_INDUSTRIES,
        'INDUSTRIES': cloud_conf.INDUSTRIES,
        'CONTENT_DATA': cloud_conf.CONTENT_DATA,
        'MULTI_ANSWER_QUESTIONS': cloud_conf.MULTI_ANSWER_QUESTIONS,
        'WEIGHTS': cloud_conf.WEIGHTS,
        'EXCLUDED_TIME_THRESHOLD': 10,
        'CONTACT_EMAIL': "Data Maturity Benchmark <no-reply@{}.appspotmail.com>".format(application_id()),
        'i18n': False,
        'GOOGLE_SHEET_EXPORT_SURVEY_FIELDS': cloud_conf.GOOGLE_SHEET_EXPORT_SURVEY_FIELDS,
        'GOOGLE_SHEET_EXPORT_RESULT_FIELDS': cloud_conf.GOOGLE_SHEET_EXPORT_RESULT_FIELDS,
        'PRODUCT_NAME': "Cloud Maturity Assessment",
        'enabled': False,
    },
}

DEFAULT_TENANT = ADS


def active_tenants():
    return {k: v for k, v in ALL_TENANTS.items() if v['enabled']}

TENANTS = active_tenants()

I18N_TENANTS = '|'.join([v['slug'] for k, v in TENANTS.items() if v['i18n']])
NOT_I18N_TENANTS = '|'.join([v['slug'] for k, v in TENANTS.items() if not v['i18n']])
ENABLED_TENANTS = '|'.join([v['slug'] for k, v in TENANTS.items()])


TENANTS_SLUG_TO_KEY = {v['slug']: k for k, v in TENANTS.items()}
TENANTS_CHOICES = [(k, v['label']) for k, v in TENANTS.items()]
