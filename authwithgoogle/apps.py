from django.apps import AppConfig


class AuthwithgoogleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authwithgoogle'
    def ready(self):
        import authwithgoogle.signals