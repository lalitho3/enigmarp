from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# WEASYPRINT
from django.template.loader import render_to_string
# MODELOS Y FORMS
from core.enigmaVentas.models import *
from core.enigmaVentas.forms import *
from xhtml2pdf import pisa


class dashboardVentas(LoginRequiredMixin,TemplateView):
    template_name = 'enigmaVentas/dashboardVentas.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ventas - Enigma'
        context['version'] = '1.0.1'
        context['prospectos'] = MantenimientoProspectos.objects.filter(Usuario=self.request.user)
        context['clientes'] = MantenimientoClientes.objects.filter(Usuario=self.request.user)
        context['creditos'] = SolicitudCredito.objects.filter(Usuario=self.request.user)
        return context


# VISTAS DEL MANTEMINTO DE PROSPECTOS


class crearProspecto(LoginRequiredMixin,FormView):
    template_name = 'enigmaVentas/formularios/prospecto.html'
    form_class = mantenimientoProspectosForm
    success_url = 'enigmaVentas:dashboardVentas'
    

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
    model = MantenimientoProspectos
    form_class = mantenimientoProspectosForm
    template_name = 'enigmaVentas/formularios/prospecto.html'
    success_url = 'enigmaVentas:dashboardVentas'


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
    prospecto = MantenimientoProspectos.objects.get(id=id)
    html_string = render_to_string('pdf/enigmaVentas/prospecto.html', {'prospecto': prospecto})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="prospecto.pdf"'
    pisa.CreatePDF(html_string, response)
    return response


# VISTAS DEL MANTEMINTO DE CLIENTES


class crearCliente(LoginRequiredMixin,FormView):
    template_name = 'enigmaVentas/formularios/cliente.html'
    form_class = mantenimiendoClientesForm
    success_url = 'enigmaVentas:dashboardVentas'
    

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
        context['title'] = 'Agregar cliente - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Registro de nuevo cliente'
        return context


class editarCliente(LoginRequiredMixin, UpdateView):
    model = MantenimientoClientes
    form_class = mantenimiendoClientesForm
    template_name = 'enigmaVentas/formularios/cliente.html'
    success_url = 'enigmaVentas:dashboardVentas'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar cliente - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Edición de cliente'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Cliente actualizado con éxito!')
        return reverse(self.success_url)


@login_required
def crearPdfClientes(request, id):
    cliente = MantenimientoClientes.objects.get(id=id)
    html_string = render_to_string('pdf/enigmaVentas/cliente.html', {'cliente': cliente})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="cliente.pdf"'
    pisa.CreatePDF(html_string, response)
    return response


# VISTAS DEL MANTENIMIENTO DE CREDITO


class crearCredito(LoginRequiredMixin,FormView):
    template_name = 'enigmaVentas/formularios/credito.html'
    form_class = solicitudCreditoForm
    success_url = 'enigmaVentas:dashboardVentas'
    

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
        context['title'] = 'Solicitud crédito - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Registro de nuevo crédito'
        return context


class editarCredito(LoginRequiredMixin, UpdateView):
    model = SolicitudCredito
    form_class = solicitudCreditoForm
    template_name = 'enigmaVentas/formularios/credito.html'
    success_url = 'enigmaVentas:dashboardVentas'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar crédito - Enigma'
        context['version'] = '1.0.1'
        context['subtitle'] = 'Edición de crédito'
        return context

    def get_success_url(self):
        messages.success(self.request, 'Crédito actualizado con éxito!')
        return reverse(self.success_url)


@login_required
def crearPdfCreditos(request, id):
    credito = SolicitudCredito.objects.get(id=id)
    html_string = render_to_string('pdf/enigmaVentas/credito.html', {'credito': credito})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="credito.pdf"'
    pisa.CreatePDF(html_string, response)
    return response


# VISTAS DEL MANTENIMIENTO DE PEDIDOS

class pedidosView(TemplateView):
    template_name = 'enigmaVentas/ventas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modulo deshabilitado'
        return context


# VISTAS DE PRODUCTOS


class verProductos(LoginRequiredMixin, TemplateView):
    template_name = 'enigmaVentas/productos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productos - Enigma'
        context['version'] = '1.0.1'
        context['productos'] = Productos.objects.all()
        return context