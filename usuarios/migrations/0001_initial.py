# Generated by Django 5.1.1 on 2024-09-15 03:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Arrendador',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.usuario')),
                ('ocupacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Arrendatario',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('arrendatario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usuarios.arrendatario')),
                ('constancia_universidad', models.CharField(max_length=100)),
                ('universidad', models.CharField(max_length=100)),
            ],
        ),
    ]
