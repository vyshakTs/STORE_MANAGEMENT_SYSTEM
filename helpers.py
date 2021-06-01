import datetime

import pytz
from django.conf import settings


def current_datetime(tformat=None):
	time = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
	return time