# Generated by Django 5.1.1 on 2024-12-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resenas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resena',
            name='fecha',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
