# Generated by Django 5.1.3 on 2024-11-14 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epica4', '0002_catalogo_id_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo',
            name='espacio_ocupado',
            field=models.IntegerField(default=0, verbose_name='Espacio ocupado'),
        ),
    ]
