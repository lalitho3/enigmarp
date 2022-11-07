from django.urls import path
from core.multipolimeros.views import *

app_name = 'multipolimeros'

urlpatterns = [
    path('dashboard/', dashboard.as_view(), name='dashboard'),
    # URLS DE PROSPECTOS
    path('crear-prospecto/', crearProspecto.as_view(), name='crear-prospecto'),
    path('editar-prospecto/<int:pk>/', editarProspecto.as_view(), name='editar-prospecto'),
    path('crear-pdf/<int:id>/', crearPdfProspectos,  name='crear-pdf'),
    # URLS DE CLIENTES
    path('crear-cliente/', crearCliente.as_view(), name='crear-cliente'),
    path('editar-cliente/<int:pk>/', editarCliente.as_view(), name='editar-cliente'),
    path('crear-pdf-cliente/<int:id>/', crearPdfClientes,  name='crear-pdf-cliente'),
    # URLS DE CREDITOS
    path('crear-credito/', crearCredito.as_view(), name='crear-credito'),
    path('editar-credito/<int:pk>/', editarCredito.as_view(), name='editar-credito'),
    path('crear-pdf-credito/<int:id>/', crearPdfCreditos,  name='crear-pdf-credito'),
]