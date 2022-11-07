from distutils.log import error
from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
# DECORADORES Y MIXINS
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#VISTAS GENERICAS
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView
#MODELS Y FORMS
from core.enigmaControl.forms import *
from django.contrib.auth.models import User
from core.enigmaControl.models import *
from django.contrib import messages
from django.db.models import Sum

from serializers.presupuestosSerializer import PresupuestoTablaSerializer, UsuariosSerializer

from rest_framework import viewsets




class dashboardControl(LoginRequiredMixin,TemplateView):
    template_name = 'enigmaControl/dashboardControl.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Control - Enigma'
        context['version'] = '1.0.1'
        context['visitas'] = controlVisitas.objects.filter(usuario=self.request.user).count()
        context['visitasTabla'] = controlVisitas.objects.filter(usuario=self.request.user)
        context['reportes'] = reportesControl.objects.filter(usuario=self.request.user).count()
        context['reportesTabla'] = reportesControl.objects.filter(usuario=self.request.user)
        return context


#  VISTAS DEL CONTROL DE VISITAS

class crearControlVisitas(LoginRequiredMixin,FormView):
    template_name = 'enigmaControl/formularios/controlVisitas.html'
    form_class = controlVisitaForm
    success_url = 'enigmaControl:indexControl'
    

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.usuario = self.request.user
        form.save()
        messages.success(self.request, '¡Registro creado exitosamente!')
        return HttpResponseRedirect(reverse(self.success_url))

    def form_invalid(self, form):
        messages.error(self.request, '¡Algo ha salido mal!')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Control de Visitas - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Registro de nueva visita'
        return context


class editarControlVisitas(LoginRequiredMixin, UpdateView):
    model = controlVisitas
    form_class = controlVisitaForm
    template_name = 'enigmaControl/formularios/controlVisitas.html'
    success_url = 'enigmaControl:indexControl'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar visita - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Edición de visita'
        return context

    def get_success_url(self):
        messages.success(self.request, '¡Visita actualizada con éxito!')
        return reverse_lazy(self.success_url)




# VISTAS DEL CONTROL DE REPORTES

class crearControlReportes(LoginRequiredMixin, FormView):
    template_name = 'enigmaControl/formularios/controlReportes.html'
    form_class = controlReportesForm
    success_url = 'enigmaControl:indexControl'

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.usuario = self.request.user
        form.save()
        messages.success(self.request, '¡Registro creado éxitosamente!')
        return HttpResponseRedirect(reverse(self.success_url))

    def form_invalid(self, form):
        messages.error(self.request, '¡Algo ha salido mal!')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Control de Visitas - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Registro de nuevo reporte'
        return context


class editarControlReportes(LoginRequiredMixin, UpdateView):
    model = reportesControl
    form_class = controlReportesForm
    template_name = 'enigmaControl/formularios/controlReportes.html'
    success_url = 'enigmaControl:indexControl'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar reporte - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Edición de reporte'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Reporte actualizado con éxito!')
        return reverse_lazy(self.success_url)

# Presupuestos

class presupuestos(LoginRequiredMixin, FormView):
    template_name = 'enigmaControl/presupuestos.html'
    form_class = presupuestoForm
    success_url = 'enigmaControl:presupuestos'

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.usuario = self.request.user
        form.save()
        messages.success(self.request, 'Presupuesto creado éxitosamente!')

        tabla = PresupuestoTabla(
            presupuesto = form.instance,
            usuario = self.request.user,
        )

        tabla.save()


        return HttpResponseRedirect(reverse(self.success_url))

    def form_invalid(self, form):
        messages.error(self.request, '¡Algo ha salido mal!')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Presupuestos - Enigma'
        context['version'] = '1.0.1'
        context['presupuestos'] = PresupuestoModelo.objects.all()
        context['presupuestosTabla'] = PresupuestoTabla.objects.filter(usuario=self.request.user)
        context['objetivoVentas'] = PresupuestoTabla.objects.filter(usuario=self.request.user).aggregate(Sum('ventasObjetivo'))
        context['realVentas'] = PresupuestoTabla.objects.filter(usuario=self.request.user).aggregate(Sum('ventasRealizadas'))
        context['objetivoCobranza'] = PresupuestoTabla.objects.filter(usuario=self.request.user).aggregate(Sum('cobranzaObjetivo'))
        context['realCobranza'] = PresupuestoTabla.objects.filter(usuario=self.request.user).aggregate(Sum('cobranzaRealizada'))
        context['userId'] = self.request.user.id
        return context

def eliminarPresupuesto(request, id):
    presupuesto = PresupuestoModelo.objects.get(id=id)
    presupuesto.delete()
    messages.success(request, 'Presupuesto eliminado con éxito!')
    return HttpResponseRedirect(reverse('enigmaControl:presupuestos'))

class crearPresupuesto(LoginRequiredMixin, FormView):
    template_name = 'enigmaControl/formularios/crearPresupuesto.html'
    form_class = presupuestoTablaForm
    success_url = 'enigmaControl:presupuestos'

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.usuario = self.request.user
        form.save()
        messages.success(self.request, 'Presupuesto creado éxitosamente!')
        return HttpResponseRedirect(reverse(self.success_url))
    
    def form_invalid(self, form):
        messages.error(self.request, messages.error)
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Presupuesto - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Registro de nuevo presupuesto'
        context['clientes'] = MantenimientoClientes.objects.filter(Usuario=self.request.user)
        return context



class actualizarPresupuesto(LoginRequiredMixin, UpdateView):
    model = PresupuestoTabla
    form_class = presupuestoTablaForm
    template_name = 'enigmaControl/formularios/crearPresupuesto.html'
    success_url = 'enigmaControl:presupuestos'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar presupuesto - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Editar Presupuesto'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Reporte actualizado con éxito!')
        return reverse_lazy(self.success_url)

def eliminarPresupuestoTabla(request, id):
    presupuesto = PresupuestoTabla.objects.get(id=id)
    presupuesto.delete()
    messages.success(request, 'Presupuesto eliminado con éxito!')
    return HttpResponseRedirect(reverse('enigmaControl:presupuestos'))


class presupuestosViewSet(viewsets.ModelViewSet):
    queryset = PresupuestoTabla.objects.all()
    serializer_class = PresupuestoTablaSerializer

class usuariosViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    


