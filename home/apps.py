from django.apps import AppConfig

class HomeConfig(AppConfig):
    name = 'home'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import create_config, create_horario, create_primeiraSecao, create_segundaSecao, create_terceiraSecao
        post_migrate.connect(create_config, sender=self)
        post_migrate.connect(create_horario, sender=self)
        post_migrate.connect(create_primeiraSecao, sender=self)
        post_migrate.connect(create_segundaSecao, sender=self)
        post_migrate.connect(create_terceiraSecao, sender=self)