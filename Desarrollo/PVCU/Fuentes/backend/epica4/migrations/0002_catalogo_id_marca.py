# Generated by Django 5.1.3 on 2024-11-14 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epica4', '0001_initial'),
        ('epica5', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo',
            name='id_marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epica5.marca', verbose_name='Marca'),
        ),
    ]