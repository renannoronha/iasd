from django.db import models
from django.contrib.sites.models import Site

# Create your models here.
class Config(models.Model):
    site = models.OneToOneField(Site, on_delete=models.PROTECT)
    nome = models.CharField('Nome do Site', max_length=255)
    telefone = models.CharField('Telefone de Contato', max_length=255)
    email = models.CharField('Email de Contato', max_length=255)
    endereco = models.CharField('Endereço da Igreja', max_length=255)
    facebook = models.CharField('URL da Página no Facebook', max_length=255, null=True, blank=True)
    youtube = models.CharField('URL do Canal do Youtube', max_length=255, null=True, blank=True)
    twitter = models.CharField('URL da conta no Twitter', max_length=255, null=True, blank=True)
    instagram = models.CharField('URL da conta no Instagram', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'