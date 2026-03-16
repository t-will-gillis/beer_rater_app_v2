from django.apps import AppConfig


class BeersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "beers"

    def ready(self):
        import beers.signals  # noqa: F401
