"""
This setting file runs the simplest devlopment environment using sqlite, default session and memory cache.
"""

from .common import *

DEBUG = True
SECRET_KEY = 'development'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}