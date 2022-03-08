from django.db import models

# Create your models here.
class Departamento(models.Model):
    departamento = models.CharField('Departamento', max_length=255)

    def __str__(self):
        return self.departamento

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

class Escala(models.Model):
    data = models.DateField('Data')
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    nome = models.CharField('Responsável', max_length=255)

    class Meta:
        verbose_name = 'Escala'
        verbose_name_plural = 'Escala'
