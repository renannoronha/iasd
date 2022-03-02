from django.apps import AppConfig


class AboutConfig(AppConfig):
    name = 'about'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import create_AboutPrimeiraSecao, create_AboutSegundaSecao, create_AboutTerceiraSecao
        post_migrate.connect(create_AboutPrimeiraSecao, sender=self)
        post_migrate.connect(create_AboutSegundaSecao, sender=self)
        post_migrate.connect(create_AboutTerceiraSecao, sender=self)