# Generated by Django 4.0.3 on 2022-05-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multipolimeros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimientoclientes',
            name='Telefono2',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Numero Telefonico 2'),
        ),
        migrations.AddField(
            model_name='mantenimientopmultip',
            name='Telefono2',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Numero Telefonico 2'),
        ),
        migrations.AddField(
            model_name='solicitudcredito',
            name='Celular',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Numero celular '),
        ),
        migrations.AddField(
            model_name='solicitudcredito',
            name='Telefono2',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Numero Telefonico 2'),
        ),
    ]
