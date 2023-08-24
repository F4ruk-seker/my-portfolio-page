from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['farukseker.gen.tr','*.up.railway.app','cvv2-production.up.railway.app',"https://cvv2-production.up.railway.app/",
                 "kisisel-production.up.railway.app",'127.0.0.1:8000','127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://*.up.railway.app','https://*.127.0.0.1:8000', 'https://farukseker.gen.tr', 'http://farukseker.gen.tr',
                        'https://kisisel-production.up.railway.app/', 'https://farukseker.gen.tr/', 'http://127.0.0.1:8000/',
                        'https://cvv2-production.up.railway.app/', 'https://pq5wifqf.up.railway.app']
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'Debug/debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'discord': {
            'level': 'ERROR',  # İstenilen seviye
            'class': 'discord_logger.DiscordLoggerDjango',  # DiscordLogger sınıfının modül yolu
            'webhook_url': DISCORD_LOGGER_WEBHOOK_URL,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['discord'],
            'level': 'ERROR',
            # 'level': 'WARN',
            'propagate': True,
        },
    },
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=env("SENTRY_DSN"),
    integrations=[DjangoIntegration(),],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('PGDATABASE'),
        'USER': env('PGUSER'),
        'PASSWORD': env('PGPASSWORD'),
        'HOST': env('PGHOST'),
        'PORT': env('PGPORT')
    }
}


