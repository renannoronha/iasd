# Generated by Django 3.1.7 on 2022-03-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ministry/', verbose_name='Imagem')),
                ('title', models.CharField(max_length=255, verbose_name='Nome do Ministério')),
                ('shortDescription', models.CharField(max_length=255, verbose_name='Descrição Curta')),
                ('about', models.TextField(blank=True, null=True, verbose_name='Sobre o Ministério')),
            ],
            options={
                'verbose_name': 'Ministério',
                'verbose_name_plural': 'Ministérios',
            },
        ),
    ]