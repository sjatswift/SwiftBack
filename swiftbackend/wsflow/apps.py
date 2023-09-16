from django.apps import AppConfig


class WsflowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wsflow'

    def ready(self):
        import wsflow.signals
        import wsflow.recievers
