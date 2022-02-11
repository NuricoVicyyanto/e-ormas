from django.apps import AppConfig


class EormasappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eormasapp'

    def ready(self):
        import eormasapp.signals  # noqa
