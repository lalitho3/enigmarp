from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.enigmaVentas.models import *

class dashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'enigmaErp/dashboard.html'
    login_url = 'auth:login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard - Enigma'
        context['version'] = '1.0.1'
        context['prospectos'] = MantenimientoProspectos.objects.filter(Usuario=self.request.user)
        context['clientes'] = MantenimientoClientes.objects.filter(Usuario=self.request.user)
        context['creditos'] = SolicitudCredito.objects.filter(Usuario=self.request.user)
        return context
