from django.db import models

# Create your models here.
class Events(models.Model):
    image = models.ImageField('Imagem do Evento', upload_to='events/', null=True, blank=True)
    title = models.CharField('Título do Evento', max_length=255)
    startTime = models.DateTimeField('Horário de Início')
    endTime = models.DateTimeField('Horário de Término')
    locationName = models.CharField('Nome do Local', max_length=255)
    locationUrl = models.CharField('Website do Local', max_length=1024)
    address = models.CharField('Endereço Completo', max_length=1024)
    details = models.TextField('Detalhes')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'