# Generated by Django 5.1.2 on 2024-10-29 03:12

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directorgeneral',
            options={'verbose_name': 'Director General', 'verbose_name_plural': 'Directores Generales'},
        ),
        migrations.AlterModelOptions(
            name='laboratorio',
            options={'verbose_name': 'Laboratorio', 'verbose_name_plural': 'Laboratorios'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2015, 1, 1))]),
        ),
    ]
