from distutils.log import Log
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, UpdateView
from django.contrib.auth.models import User
from core.enigmaVentas.models import *
from core.enigmaControl.models import PresupuestoModelo, PresupuestoTabla
from django.db.models import Sum


class dashboardAdmin(LoginRequiredMixin, TemplateView):
    template_name = 'enigmaAdmin/dashboardAdmin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Administración - Enigma'
        context['version'] = '1.0.1'
        context['usuarios'] = User.objects.all()
        context['prospectos'] = MantenimientoProspectos.objects.all().count()
        context['clientes'] = MantenimientoClientes.objects.all().count()
        context['creditos'] = SolicitudCredito.objects.all().count()
        context['presupuestos'] = PresupuestoTabla.objects.all()
        return context

        


class gestionPersonal(LoginRequiredMixin, TemplateView):
    template_name = 'enigmaAdmin/gestion.html'

    def get_context_data(self, pk, **kwargs,):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gestión de Personal - Enigma'
        context['version'] = '1.0.1'
        context['usuario'] = User.objects.get(pk=pk)
        context['clientes'] = MantenimientoClientes.objects.filter(Usuario = User.objects.get(pk=pk))
        context['presupuestos'] = PresupuestoModelo.objects.all()
        context['presupuestosTabla'] = PresupuestoTabla.objects.filter(usuario=User.objects.get(pk=pk))
        return context 

class administrarPresupuestos(LoginRequiredMixin, TemplateView):
    template_name = 'enigmaAdmin/administrarPresupuestos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Administrar Presupuestos - Enigma'
        context['version'] = '1.0.1'
        context['usuarios'] = User.objects.all()
        context['presupuestosMes'] = PresupuestoModelo.objects.all()
        context['ventasObjetivo'] = PresupuestoTabla.objects.all().aggregate(Sum('ventasObjetivo'))
        context['ventasRealizadas'] = PresupuestoTabla.objects.all().aggregate(Sum('ventasRealizadas'))
        context['cobranzaObjetivo'] = PresupuestoTabla.objects.all().aggregate(Sum('cobranzaObjetivo'))
        context['cobranzaRealizada'] = PresupuestoTabla.objects.all().aggregate(Sum('cobranzaRealizada'))
        return context

class tablaPresupuestos(LoginRequiredMixin, TemplateView):
    template_name = 'enigmaAdmin/tablaPresupuestos.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tabla de Presupuestos - Enigma'
        context['version'] = '1.0.1'
        context['usuario'] = User.objects.get(pk=pk)
        context['presupuestos'] = PresupuestoTabla.objects.filter(usuario=User.objects.get(pk=pk))
        return context