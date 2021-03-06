# Generated by Django 3.1.7 on 2022-02-28 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Site')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone de Contato')),
                ('email', models.CharField(max_length=255, verbose_name='Email de Contato')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço da Igreja')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True, verbose_name='URL da Página no Facebook')),
                ('youtube', models.CharField(blank=True, max_length=255, null=True, verbose_name='URL do Canal do Youtube')),
                ('twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='URL da conta no Twitter')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='URL da conta no Instagram')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Configuração',
                'verbose_name_plural': 'Configurações',
            },
        ),
    ]
