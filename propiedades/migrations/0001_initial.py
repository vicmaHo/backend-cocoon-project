# Generated by Django 5.1.1 on 2024-09-15 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_vivienda', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('direccion', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('estado', models.CharField(max_length=50)),
                ('reglas', models.TextField()),
                ('servicios', models.TextField()),
                ('fotos', models.CharField(max_length=100)),
                ('videos', models.CharField(max_length=100)),
                ('arrendador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.arrendador')),
            ],
        ),
    ]
