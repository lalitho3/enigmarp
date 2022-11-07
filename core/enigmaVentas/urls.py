from django.urls import path
from core.enigmaVentas.views import *

app_name = 'enigmaVentas'

urlpatterns = [
    path('', dashboardVentas.as_view(), name='dashboardVentas'),
    # MANTENIMIENTO DE PROSPECTOS
    path('crear-prospecto/', crearProspecto.as_view(), name='crearProspecto'),
    path('editar-prospecto/<int:pk>/', editarProspecto.as_view(), name='editarProspecto'),
    path('pdf-prospecto/<int:id>/', crearPdfProspectos, name='pdfProspecto'),
    # MANTENIMIENTO DE CLIENTES
    path('crear-cliente/', crearCliente.as_view(), name='crearCliente'),
    path('editar-cliente/<int:pk>/', editarCliente.as_view(), name='editarCliente'),
    path('pdf-cliente/<int:id>/', crearPdfClientes, name='pdfCliente'),
    # SOLICITUD DE CREDITO
    path('solicitud-credito/', crearCredito.as_view(), name='solicitudCredito'),
    path('editar-credito/<int:pk>/', editarCredito.as_view(), name='editarCredito'),
    path('pdf-credito/<int:id>/', crearPdfCreditos, name='pdfCredito'),
    # PEDIDOS
    path('crear-pedido/', pedidosView.as_view(), name='crearPedido'),
    # PRODUCTOS
    path('ver-productos/', verProductos.as_view(), name='verProductos'),
]