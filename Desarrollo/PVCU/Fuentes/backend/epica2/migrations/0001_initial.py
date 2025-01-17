# Generated by Django 5.1.3 on 2024-11-13 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('siglas', models.CharField(max_length=20, verbose_name='Siglas')),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Facultades',
                'db_table': 'Facultad',
            },
        ),
        migrations.CreateModel(
            name='EscuelaProfesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('id_facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epica2.facultad', verbose_name='Facultad')),
            ],
            options={
                'verbose_name': 'Escuela Profesional',
                'verbose_name_plural': 'Escuelas Profesionales',
                'db_table': 'EscuelaProfesional',
            },
        ),
    ]
