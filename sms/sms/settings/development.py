from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'SMS',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

# Loads SECRET_KEY from .env file
# SECRET_KEY = get_env_variable('SECRET_KEY')
