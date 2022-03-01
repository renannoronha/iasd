from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField('Imagem', upload_to='gallery/')
    ativo = models.BooleanField('Ativo', default=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galeria de Fotos'