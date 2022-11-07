from enum import unique
from pyexpat import model
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from django import forms

from core.enigmaVentas.models import MantenimientoClientes

from django.db.models import Sum


class controlVisitas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarioVisitas')
    id = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=100, blank=False)
    nombreVisita = models.CharField(max_length=100)
    razonVisita = models.CharField(max_length=200)
    duracionVisita = models.TimeField()
    observaciones = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Control de Visitas'
        verbose_name_plural = 'Control de Visitas'
        ordering = ['-id']

    def to_json(self):
        item = model_to_dict
        item['id'] = self.id
        item['usuario'] = self.usuario.username
        item['fecha'] = self.fecha
        item['nombreVisita'] = self.nombreVisita
        item['razonVisita'] = self.razonVisita
        item['duracionVisita'] = self.duracionVisita
        item['observaciones'] = self.observaciones
        return item

    def __str__(self):
        return f'Visita de {self.nombreVisita} - {self.fecha}'


class reportesControl(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarioReportes')
    id = models.AutoField(primary_key=True)
    fechaReporte = models.CharField(max_length=100, blank=False)
    nombreReporte = models.CharField(max_length=200)
    notificarReporte =models.CharField(max_length=200)
    descripcionReporte = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Reportes de Control'
        verbose_name_plural = 'Reportes de Control'

    def __str__(self):
        return f'Reporte de {self.nombreReporte} - {self.fechaReporte}'


MESES = (
    ('Enero', 'Enero'),
    ('Febrero', 'Febrero'),
    ('Marzo', 'Marzo'),
    ('Abril', 'Abril'),
    ('Mayo', 'Mayo'),
    ('Junio', 'Junio'),
    ('Julio', 'Julio'),
    ('Agosto', 'Agosto'),
    ('Septiembre', 'Septiembre'),
    ('Octubre', 'Octubre'),
    ('Noviembre', 'Noviembre'),
    ('Diciembre', 'Diciembre')
)

class PresupuestoModelo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarioPresupuesto')
    id = models.AutoField(primary_key=True)
    mesPresupuesto = models.CharField(max_length=100, choices=MESES, default='Enero', unique=True)

    class Meta:
        verbose_name = 'Presupuesto'
        verbose_name_plural = 'Presupuestos'

    def __str__(self):
        return f'Presupuesto de {self.mesPresupuesto}'


class PresupuestoTabla(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarioPresupuestos')
    id = models.AutoField(primary_key=True)
    presupuesto = models.ForeignKey(PresupuestoModelo, on_delete=models.CASCADE, related_name='presupuesto')
    razonSocial = models.ForeignKey(MantenimientoClientes, on_delete=models.CASCADE, related_name='razonSocial', null=True)
    ventasObjetivo = models.BigIntegerField(blank=True, null=True)
    ventasRealizadas = models.BigIntegerField(blank=True, null=True)
    cobranzaObjetivo = models.BigIntegerField(blank=True, null=True)
    cobranzaRealizada = models.BigIntegerField(blank=True, null=True)

    def getVentasPercentage(self):
        try:
            return round((self.ventasRealizadas / self.ventasObjetivo) * 100, 2)
        except:
            return 0

    def getCobranzaPercentage(self):
        try:
            return round((self.cobranzaRealizada / self.cobranzaObjetivo) * 100, 2)
        except:
            return 0

    @property
    def get_ventas(self):
        return sum([item.ventasRealizadas for item in self.presupuesto.presupuestotabla_set.all()])


    class Meta:
        verbose_name = 'Presupuestos Tabla'
        verbose_name_plural = 'Presupuestos Tabla'

    def __str__(self):
        return f'Presupuesto de {self.usuario.username} - {self.razonSocial}'


