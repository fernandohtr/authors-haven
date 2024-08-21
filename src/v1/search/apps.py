from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SearchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "v1.search"
    verbose_name = _("Search")

    @staticmethod
    def ready():
        from v1.search import signals  # noqa
