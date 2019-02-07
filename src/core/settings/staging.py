from core.settings.live import *  # noqa

MIDDLEWARE_CLASSES = tuple(
    list(MIDDLEWARE_CLASSES) +
    [
        'core.middleware.UsersRestrictionMiddleware',
    ])

ALLOWED_AUTH_DOMAINS = [
    'google.com',
    'potatolondon.com',
]

DJANGAE_CREATE_UNKNOWN_USER = True

# override QUALTRICS_SURVEY_ID for staging environment
TENANTS['ads']['QUALTRICS_SURVEY_ID'] = 'SV_beH0HTFtnk4A5rD'
