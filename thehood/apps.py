from django.apps import AppConfig


class ThehoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'thehood'

    def ready(self):
        import thehood.signals  
        