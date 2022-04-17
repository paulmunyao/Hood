from django.apps import AppConfig


class ThehoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'thehood'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals   
        