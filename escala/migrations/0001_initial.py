# Generated by Django 3.1.7 on 2022-03-08 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=255, verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Escala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('nome', models.CharField(max_length=255, verbose_name='Responsável')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='escala.departamento')),
            ],
            options={
                'verbose_name': 'Escala',
                'verbose_name_plural': 'Escala',
            },
        ),
    ]
