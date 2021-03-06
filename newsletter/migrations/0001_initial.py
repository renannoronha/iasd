# Generated by Django 3.1.7 on 2022-03-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ministry/', verbose_name='Imagem')),
                ('date', models.DateField(verbose_name='Data')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('shortDescription', models.CharField(max_length=255, verbose_name='Descrição Curta')),
                ('text', models.TextField(verbose_name='Texto')),
                ('videoLink', models.CharField(blank=True, max_length=255, null=True, verbose_name='Link do Vídeo')),
            ],
            options={
                'verbose_name': 'Ministério',
                'verbose_name_plural': 'Ministérios',
            },
        ),
    ]
