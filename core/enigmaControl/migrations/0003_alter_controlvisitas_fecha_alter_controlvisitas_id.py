# Generated by Django 4.0.3 on 2022-04-25 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('enigmaControl', '0002_controlvisitas_usuario_alter_controlvisitas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlvisitas',
            name='fecha',
            field=models.DateField(verbose_name=datetime.datetime(2022, 4, 25, 15, 4, 31, 541293, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='controlvisitas',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
