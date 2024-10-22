from .base import *

DEBUG = False

ADMINS = (
    ('rpsts', 'rupesh@testpress.in'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'educa',
       'USER': 'educa',
       'PASSWORD': 'rpsts2016',
   }
}

# SSL config
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True