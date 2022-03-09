from django.db import models

# Create your models here.
class Testemunho(models.Model):
    image = models.ImageField('Image', upload_to='testemunho/')
    name = models.CharField('Nome', max_length=255)
    shortDescription = models.CharField('Descrição Curta', max_length=255)
    description = models.TextField('Testemunho')
    video = models.CharField('URL do vídeo do Testemunho (Youtube)', max_length=255, null=True, blank=True)
