from django.apps import AppConfig


class ChechoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chechout'

    def ready(self):
        import checkout.signals
