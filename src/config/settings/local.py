import os

from config.settings.base import *  # noqa

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "7TQK-V4W9HZoRTcfVNfq4L5HVzDizjvnxPtyM4fdoPo2bezVON5bqA")
DEBUG = True
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
]
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", default="mailhog")
EAMIL_PORT = os.environ.get("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "fernandohtr@gmail.com"
DOMAIN = os.environ.get("DOMAIN")
SITE_NAME = "Authors Haven"
