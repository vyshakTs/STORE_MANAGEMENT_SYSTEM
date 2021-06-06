from .base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'github_actions',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Loads SECRET_KEY from .env file
# SECRET_KEY = get_env_variable('SECRET_KEY')

SECRET_KEY = str(os.environ.get('SECRET_KEY'))
