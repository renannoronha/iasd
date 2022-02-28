# Generated by Django 3.1.7 on 2022-02-28 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('home', '0004_horariosculto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.IntegerField(default=1, verbose_name='Número na Sequência')),
                ('backgroundImage', models.ImageField(upload_to='banner/', verbose_name='Imagem de Fundo')),
                ('upperText', models.CharField(blank=True, max_length=255, null=True, verbose_name='Texto Superior')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('subtitulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtítulo')),
                ('botaoLink', models.CharField(blank=True, max_length=255, null=True, verbose_name='Link do Botão')),
                ('botaoText', models.CharField(blank=True, max_length=255, null=True, verbose_name='Texto do Botão')),
                ('ativo', models.BooleanField(blank=True, default=True, null=True, verbose_name='Ativo')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
        ),
    ]
