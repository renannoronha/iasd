# Generated by Django 3.1.7 on 2022-03-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='shortDescription',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição Curta'),
        ),
    ]
