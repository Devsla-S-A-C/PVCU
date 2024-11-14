# Generated by Django 5.1.3 on 2024-11-14 00:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Informacion')),
                ('espacio_extra', models.IntegerField(verbose_name='Espacio adicional')),
                ('duracion', models.IntegerField(verbose_name='Duración en meses')),
                ('precio', models.FloatField(verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Planes',
                'db_table': 'Plan',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Informacion')),
                ('logo', models.URLField(verbose_name='Logo')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Dueño')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'db_table': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_final', models.DateTimeField()),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epica5.marca', verbose_name='Marca')),
                ('id_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epica5.plan', verbose_name='Tipo de plan')),
            ],
            options={
                'verbose_name': 'Membresia',
                'verbose_name_plural': 'Membresias',
                'db_table': 'Membresia',
            },
        ),
    ]
