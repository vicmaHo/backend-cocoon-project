# Generated by Django 5.1.1 on 2024-12-12 23:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('propiedades', '0003_propiedad_cantidad_banos_and_more'),
        ('usuarios', '0003_usuario_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField()),
                ('comentario', models.TextField()),
                ('fecha', models.DateField()),
                ('arrendatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.arrendatario')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedades.propiedad')),
            ],
        ),
    ]
