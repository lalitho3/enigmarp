# Generated by Django 4.0.3 on 2022-05-02 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enigmaControl', '0008_reportescontrol'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='controlvisitas',
            options={'ordering': ['-id'], 'verbose_name': 'Control de Visitas', 'verbose_name_plural': 'Control de Visitas'},
        ),
    ]
