from django.db import models

# Create your models here.
class News(models.Model):
    image = models.ImageField('Imagem', upload_to='ministry/', null=True, blank=True)
    date = models.DateField('Data')
    title = models.CharField('Título', max_length=255)
    shortDescription = models.CharField('Descrição Curta', max_length=255, null=True, blank=True)
    text = models.TextField('Texto')
    videoLink = models.CharField('Link do Vídeo', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Ministério'
        verbose_name_plural = 'Ministérios'