# Generated by Django 5.1.3 on 2024-11-14 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epica4', '0004_articulo_precio'),
        ('epica5', '0003_alter_membresia_fecha_inicio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogo',
            options={'verbose_name': 'Catálogo', 'verbose_name_plural': 'Catálogos'},
        ),
        migrations.AlterField(
            model_name='catalogo',
            name='id_marca',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='epica5.marca', verbose_name='Marca'),
        ),
    ]
