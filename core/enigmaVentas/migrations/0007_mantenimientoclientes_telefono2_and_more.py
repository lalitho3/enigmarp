# Generated by Django 4.0.3 on 2022-05-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enigmaVentas', '0006_remove_solicitudcredito_documentosentregados_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimientoclientes',
            name='Telefono2',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Numero Telefonico 2'),
        ),
        migrations.AddField(
            model_name='mantenimientoprospectos',
            name='Telefono2',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Numero Telefonico 2'),
        ),
        migrations.AddField(
            model_name='solicitudcredito',
            name='Telefono2',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Numero Telefonico 2'),
        ),
    ]
