from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "bokaforlag.users"
    verbose_name = "Notendur"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
