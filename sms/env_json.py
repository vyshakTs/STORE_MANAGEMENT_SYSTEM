import json
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

# PATH_TO_JSON = Path(__file__).resolve().parent.parent

# Reading Json file.
with open('secrets.json') as f:
    secrets = json.loads(f.read())
    
# Checking environment variable exists in json file.
def get_secret(setting, secrets=secrets):
    # Get secret variable or return explicit exception.
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f'Set the {setting} environment variable.'
        raise ImproperlyConfigured(error_msg)