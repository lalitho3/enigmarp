# Generated by Django 4.0.3 on 2022-04-26 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enigmaControl', '0007_alter_controlvisitas_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportesControl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaReporte', models.CharField(max_length=100)),
                ('nombreReporte', models.CharField(max_length=200)),
                ('notificarReporte', models.CharField(max_length=200)),
                ('descripcionReporte', models.TextField(max_length=200)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioReportes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reportes de Control',
                'verbose_name_plural': 'Reportes de Control',
            },
        ),
    ]