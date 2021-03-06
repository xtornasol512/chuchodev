from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [os.environ["ALLOWED_HOST"], "127.0.0.1"]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


