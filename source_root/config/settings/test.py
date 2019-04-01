"""
This config file runs the simplest test environment using sqlite, and db-based
sessions.
"""
import logging

from .common import *

SECRET_KEY = 'Test'

# Silence noisy logs to make troubleshooting easier when tests fail.
LOGGING['handlers']['console']['level'] = 'DEBUG'

LOG_OVERRIDES = [
    ('factory.generate', logging.ERROR),
    ('factory.containers', logging.ERROR),
]
for log_name, log_level in LOG_OVERRIDES:
    logging.getLogger(log_name).setLevel(log_level)

# Nose Test Runner
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'testdb.sqlite3'),
    }
}