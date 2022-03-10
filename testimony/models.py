from django.db import models

# Create your models here.
class testimony(models.Model):
    image = models.ImageField('Image', upload_to='testimony/')
    name = models.CharField('Nome', max_length=255)
    shortDescription = models.CharField('Descrição Curta', max_length=255)
    description = models.TextField('testimony')
    video = models.CharField('URL do vídeo do testimony (Youtube)', max_length=255, null=True, blank=True)
