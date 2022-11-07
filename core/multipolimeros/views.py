from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, UpdateView
from core.multipolimeros.models import MantenimientoClientes, MantenimientoPMultiP, SolicitudCredito
from core.multipolimeros.forms import *
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from xhtml2pdf import pisa


class dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'multiP/dashboard.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard - Multipolimeros'
        context['version'] = '1.0.1'
        context['prospectos'] = MantenimientoPMultiP.objects.filter(Usuario=self.request.user)
        context['clientes'] = MantenimientoClientes.objects.filter(Usuario=self.request.user)
        context['creditos'] = SolicitudCredito.objects.filter(Usuario=self.request.user)
        return context


# VISTAS DEL MANTEMINTO DE PROSPECTOS

class crearProspecto(LoginRequiredMixin,FormView):
    template_name = 'multiP/formularios/prospecto.html'
    form_class = MantenimientoMultiPForm
    success_url = 'multipolimeros:dashboard'
    

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.Usuario = self.request.user
        form.save()
        messages.success(self.request, '¡Prospecto creado exitosamente!')
        return HttpResponseRedirect(reverse(self.success_url))

    def form_invalid(self, form):
        messages.error(self.request, '¡Algo ha salido mal!')
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar prospecto - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Registro de nuevo prospecto'
        return context


class editarProspecto(LoginRequiredMixin, UpdateView):
    model = MantenimientoPMultiP
    form_class = MantenimientoMultiPForm
    template_name = 'multiP/formularios/prospecto.html'
    success_url = 'multipolimeros:dashboard'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar prospecto - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Edición de prospecto'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Prospecto actualizado con éxito!')
        return reverse(self.success_url)

@login_required
def crearPdfProspectos(request, id):
    prospecto = MantenimientoPMultiP.objects.get(id=id)
    html_string = render_to_string('multiP/pdf/prospectos.html', {'prospecto': prospecto})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="prospecto.pdf"'
    pisa.CreatePDF(html_string, response)
    return response


# VISTAS DEL MANTEMINTO DE CLIENTES


class crearCliente(LoginRequiredMixin,FormView):
    template_name = 'multiP/formularios/cliente.html'
    form_class = MantenimientoClientesForm
    success_url = 'multipolimeros:dashboard'
    

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.Usuario = self.request.user
        form.save()
        messages.success(self.request, 'Cliente creado exitosamente!')
        return HttpResponseRedirect(reverse(self.success_url))

    def form_invalid(self, form):
        messages.error(self.request, 'Faltan campos por llenar!')
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar cliente - Multipolimeros'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Registro de nuevo cliente'
        return context


class editarCliente(LoginRequiredMixin, UpdateView):
    model = MantenimientoClientes
    form_class = MantenimientoClientesForm
    template_name = 'multiP/formularios/cliente.html'
    success_url = 'multipolimeros:dashboard'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar cliente - Multipolimeros'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Edición de cliente'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Cliente actualizado con éxito!')
        return reverse(self.success_url)


@login_required
def crearPdfClientes(request, id):
    cliente = MantenimientoClientes.objects.get(id=id)
    html_string = render_to_string('multiP/pdf/cliente.html', {'cliente': cliente})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="cliente.pdf"'
    pisa.CreatePDF(html_string, response)
    return response


# VISTAS DEL CREDITO


class crearCredito(LoginRequiredMixin,FormView):
    template_name = 'multiP/formularios/credito.html'
    form_class = CreditoForm
    success_url = 'multipolimeros:dashboard'
    

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.Usuario = self.request.user
        form.save()
        messages.success(self.request, 'Solicitud de crédito creada exitosamente!')
        return HttpResponseRedirect(reverse(self.success_url))

    def form_invalid(self, form):
        messages.error(self.request, '¡Algo ha salido mal!')
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Solicitud crédito - Multipolimeros'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Registro de nuevo crédito'
        return context



class editarCredito(LoginRequiredMixin, UpdateView):
    model = SolicitudCredito
    form_class = CreditoForm
    template_name = 'multiP/formularios/credito.html'
    success_url = 'multipolimeros:dashboard'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar crédito - Multipolimeros'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Edición de crédito'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Crédito actualizado con éxito!')
        return reverse(self.success_url)


@login_required
def crearPdfCreditos(request, id):
    credito = SolicitudCredito.objects.get(id=id)
    html_string = render_to_string('multiP/pdf/credito.html', {'credito': credito})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="credito.pdf"'
    pisa.CreatePDF(html_string, response)
    return response
