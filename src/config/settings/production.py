import os

from .base import *  # noqa

SIX_DAYS_IN_SECONDS = 60 * 60 * 24 * 6  # 518400

ADMINS = [
    ("Fernando Toledo", "fernandohtr@gmail.com"),
]
CSRF_TRUSTED_ORIGINS = ["https://authorshaven.fernandohtr.com"]
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS")
ADMIN_URL = os.environ.get("DJANGO_ADMIN_URL")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", default="Fernando Toledo <fernandohtr@gmail.com>")
SITE_NAME = "Authors Haven"
SERVER_EMAIL = os.environ.get("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
DEFAULT_FROM_EMAIL = "fernandohtr@gmail.com"
EMAIL_SUBJECT_PREFIX = os.environ.get("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Authors Haven]")
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("SMTP_MAILGUN_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = True
DOMAIN = os.environ.get("DOMAIN")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "[%(levelname)s] [%(asctime)s] [%(module)s] " "[%(process)d] [%(thread)d] %(message)s",
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["required_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
