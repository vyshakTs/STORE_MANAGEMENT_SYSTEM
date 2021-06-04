from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

# DATABASES = {
#     "default": env.dj_db_url("DATABASE_URL")
# }
# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
