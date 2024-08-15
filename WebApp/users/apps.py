from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WebApp.users'

    def ready(self):
        import WebApp.users.signals
