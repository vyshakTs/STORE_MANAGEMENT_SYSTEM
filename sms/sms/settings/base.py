"""
Django settings for sms project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
# import apps
from pathlib import Path

from env_json import get_secret

#from dotenv import load_dotenv


## Loads environment variables from .env file.
#load_dot_env(verbose=True)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


#----------------------------------------------------------------------
''' Below block of code is used to get environment variables from .env file

Checks environment variables exists in .env file.
def get_env_variable(var_name):
    # Get the environment variable or return exception.
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f'Set the {var_name} environment variable.' 
        raise ImproperlyConfigured(error_msg)

Loading the SECRET_KEY from .env
SECRET_KEY = get_env_variable('SECRET_KEY') '''
#----------------------------------------------------------------------


# Loading SECRET_KEY from secrets.json file.
SECRET_KEY = get_secret('SECRET_KEY')


DEBUG = get_secret('DEBUG')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

ALLOWED_HOSTS = ['127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # all auth
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    
    # Local
    'apps.accounts.apps.AccountsConfig',
    'apps.storemaster.apps.StoremasterConfig',
    'apps.stores.apps.StoresConfig',
    'apps.products.apps.ProductsConfig',
    'apps.orders.apps.OrdersConfig',
    'apps.customers.apps.CustomersConfig',
    
    # Template rendering
    'widget_tweaks',
    'crispy_forms'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'sms.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates/',
            BASE_DIR / 'sms/apps/accounts/templates/',
            BASE_DIR / 'sms/apps/accounts/templates/account',
            BASE_DIR / 'sms/apps/storemaster/templates/',
            BASE_DIR / 'sms/apps/store/templates/',
            BASE_DIR / 'sms/apps/products/templates/',
            BASE_DIR / 'sms/apps/orders/templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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



# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIR = BASE_DIR / 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static/']


# For uploading documents.
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Disable ssl mode if DJANGO_SSL_MODE is set to false.
if os.environ.get('DJANGO_SSL_MODE') == False:
    del DATABASES['default']['OPTIONS']['sslmode']
    
    
# django-allauth settings
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in django admin, regardless of `allauth`.
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication method, such as login by email.
    'allauth.account.auth_backends.AuthenticationBackend',
    )

AUTH_USER_MODEL = 'accounts.User'

SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = '/home/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 500
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = False
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = get_anonymous_login_redirect_url('LOGIN_REDIRECT_URL')
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = get_login_redirect_url('LOGIN_REDIRECT_URL')
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'