"""
Django development settings for Bucki project.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from .base import *  # NOQA
from .base import env


# Development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default= 'django-insecure-odvp9+hdq=s+l8c_wq2wf&4%^9y*66nncp@n^2#!1xanp*hc2j')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allowed hosts
# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-ALLOWED_HOSTS
ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
]

# Cache
# https://docs.djangoproject.com/en/3.2/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# Email
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# django-extensions
INSTALLED_APPS += ['django_extensions']  # noqa F405
