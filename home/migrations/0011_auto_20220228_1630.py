# Generated by Django 3.1.7 on 2022-02-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_terceirasecao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segundasecao',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Imagem de Fundo'),
        ),
    ]
