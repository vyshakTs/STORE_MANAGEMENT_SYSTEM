import dj_database_url

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

# DATABASES = {
#     "default": env.dj_db_url("DATABASE_URL")
# }

DATABASES = {'default': dj_database_url.config()}