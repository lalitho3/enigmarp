# Generated by Django 4.0.3 on 2022-04-25 14:57

import datetime
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='controlVisitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default= timezone.now)),
                ('nombreVisita', models.CharField(max_length=100)),
                ('razonVisita', models.CharField(max_length=200)),
                ('duracionVisita', models.CharField(max_length=100)),
                ('observaciones', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'Control de Visitas',
                'verbose_name_plural': 'Control de Visitas',
            },
        ),
    ]
