from django.db import models

# Create your models here.
class Sermon(models.Model):
    title = models.CharField('Título', max_length=255)
    speaker = models.CharField('Orador', max_length=255)
    date = models.DateField('Data')
    description = models.TextField('Descrição', null=True, blank=True)
    link = models.CharField('Link', max_length=1024)

    class Meta:
        verbose_name = 'Sermão'
        verbose_name_plural = 'Sermões'