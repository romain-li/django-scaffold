from .common import *

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '{Generate it by your self}'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_NAME', 'root'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', None),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.environ.get('MEMCACHE_LOCATION', 'localhost:11211'),
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 10240,
        },
    },
}