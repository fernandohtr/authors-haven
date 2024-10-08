from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "v1.profiles"
    verbose_name = _("Profiles")

    @staticmethod
    def ready():
        from v1.profiles import signals  # noqa
