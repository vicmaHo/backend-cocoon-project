# Generated by Django 5.1.1 on 2024-12-07 20:06

import propiedades.nube
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='cantidad_banos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='cantidad_habitaciones',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='cantidad_huespedes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='fotos',
            field=models.ImageField(storage=propiedades.nube.MediaStorage(), upload_to='fotos_propiedades/'),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='videos',
            field=models.FileField(storage=propiedades.nube.MediaStorage(), upload_to='videos_propiedades/'),
        ),
    ]