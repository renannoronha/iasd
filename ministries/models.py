from django.db import models

# Create your models here.
class Ministry(models.Model):
    image = models.ImageField('Imagem', upload_to='ministry/')
    title = models.CharField('Nome do Ministério', max_length=255)
    shortDescription = models.CharField('Descrição Curta', max_length=255)
    about = models.TextField('Sobre o Ministério', null=True, blank=True)

    class Meta:
        verbose_name = 'Ministério'
        verbose_name_plural = 'Ministérios'