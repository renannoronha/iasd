from django.db import models
from django.contrib.sites.models import Site

# Create your models here.
class AboutPrimeiraSecao(models.Model):
    site = models.OneToOneField(Site, on_delete=models.PROTECT)
    
    icone1 = models.CharField('Ícone 1', max_length=255)
    titulo1 = models.CharField('Título 1', max_length=255)
    subtitulo1 = models.CharField('Subtitulo 1', max_length=255, null=True, blank=True)
    texto1 = models.CharField('Texto 1', max_length=255)
    
    icone2 = models.CharField('Ícone 2', max_length=255)
    titulo2 = models.CharField('Título 2', max_length=255)
    subtitulo2 = models.CharField('Subtitulo 2', max_length=255, null=True, blank=True)
    texto2 = models.CharField('Texto 2', max_length=255, null=True, blank=True)
    
    icone3 = models.CharField('Ícone 3', max_length=255)
    titulo3 = models.CharField('Título 3', max_length=255)
    subtitulo3 = models.CharField('Subtitulo 3', max_length=255, null=True, blank=True)
    texto3 = models.CharField('Texto 3', max_length=255)

    servicesTitulo = models.CharField('Título Serviço (quadro direito)', max_length=255)
    servicesSubtitulo = models.CharField('Subtitulo Serviço (quadro direito)', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Seção 1'
        verbose_name_plural = 'Seção 1'

class AboutSegundaSecao(models.Model):
    site = models.OneToOneField(Site, on_delete=models.PROTECT)
    image = models.ImageField('Imagem de Fundo', upload_to='about/', null=True, blank=True)
    upperText = models.CharField('Texto Superior', max_length=255, null=True, blank=True)
    titulo = models.CharField('Título', max_length=255)
    texto = models.TextField('Texto', default='')
    botaoLink = models.CharField('Link do Botão', max_length=255, null=True, blank=True)
    botaoText = models.CharField('Texto do Botão', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Seção 2'
        verbose_name_plural = 'Seção 2'

class AboutTerceiraSecao(models.Model):
    site = models.OneToOneField(Site, on_delete=models.PROTECT)
    titulo = models.CharField('Título', max_length=255)
    dado1 = models.CharField('Nome 1', max_length=255, null=True, blank=True)
    valor1 = models.IntegerField('Valor 1', default=1, null=True, blank=True)
    dado2 = models.CharField('Nome 2', max_length=255, null=True, blank=True)
    valor2 = models.IntegerField('Valor 2', default=1, null=True, blank=True)
    dado3 = models.CharField('Nome 3', max_length=255, null=True, blank=True)
    valor3 = models.IntegerField('Valor 3', default=1, null=True, blank=True)
    dado4 = models.CharField('Nome 4', max_length=255, null=True, blank=True)
    valor4 = models.IntegerField('Valor 4', default=1, null=True, blank=True)

    class Meta:
        verbose_name = 'Seção 3'
        verbose_name_plural = 'Seção 3'

class Pastor(models.Model):
    nome = models.CharField('Nome', max_length=255)
    cargo = models.CharField('Cargo', max_length=255)
    foto = models.ImageField('Foto', upload_to='pastor/', null=True, blank=True)

    class Meta:
        verbose_name = 'Pastor'
        verbose_name_plural = 'Pastor'