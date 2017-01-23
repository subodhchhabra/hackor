"""
Django settings for hackor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import random
import string

from .local_settings import SECRET_KEY, DATABASES, DEBUG
assert(len(DATABASES))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def random_str(n=50):
    chars = ''.join([string.ascii_letters, string.digits, string.punctuation]
                    ).replace('\'', '').replace('"', '').replace('\\', '')
    return ''.join([random.SystemRandom().choice(chars) for i in range(n)])


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY or os.getenv('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    # need to store the new key somehwere that the other gunicorn instances can find it too!
    os.environ["DJANGO_SECRET_KEY"] = random_str()
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG or False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['totalgood.org', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'rest_framework',
    'rest_framework_gis',
    'django_extensions',
    'url_filter',
    'pacs',
    'guess',
    'bicycle_theft',
    'predict_year',
    'twitterbot',
    'twote',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'hackor.urls'

WSGI_APPLICATION = 'hackor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = DATABASES if len(DATABASES) else {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DATABASE_NAME'),
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD')
    },
}


TEST = {}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'collected-static')

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'PAGE_SIZE': 30,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer', ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',)
}
APPS_TO_REST = ('pacs',)
