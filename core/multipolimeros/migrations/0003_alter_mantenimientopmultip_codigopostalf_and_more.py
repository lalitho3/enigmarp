# Generated by Django 4.0.3 on 2022-05-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multipolimeros', '0002_mantenimientoclientes_telefono2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimientopmultip',
            name='CodigoPostalF',
            field=models.IntegerField(blank=True, null=True, verbose_name='Código Postal Fabrica'),
        ),
        migrations.AlterField(
            model_name='mantenimientopmultip',
            name='ColoniaF',
            field=models.CharField(blank=True, max_length=200, verbose_name='Colonia Fabrica'),
        ),
        migrations.AlterField(
            model_name='mantenimientopmultip',
            name='DireccionFabrica',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección Fabrica'),
        ),
        migrations.AlterField(
            model_name='mantenimientopmultip',
            name='EstadoF',
            field=models.CharField(blank=True, max_length=100, verbose_name='Estado Fabrica'),
        ),
        migrations.AlterField(
            model_name='mantenimientopmultip',
            name='MunicipioF',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Municipio Fabrica'),
        ),
        migrations.AlterField(
            model_name='mantenimientopmultip',
            name='NumExtF',
            field=models.CharField(blank=True, max_length=6, verbose_name='Numero Exterior Fabrica'),
        ),
        migrations.AlterField(
            model_name='mantenimientopmultip',
            name='NumIntF',
            field=models.CharField(blank=True, max_length=6, verbose_name='Numero Interior Fabrica'),
        ),
    ]
