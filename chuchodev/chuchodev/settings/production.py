from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = [
    os.environ["ALLOWED_HOST"],
    os.environ["HEROKU_APP_NAME"] + ".herokuapp.com",]

# STATICS
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


