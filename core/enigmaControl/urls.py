from django.urls import path
from core.enigmaControl.views import *

app_name = 'enigmaControl'

urlpatterns = [
    path('', dashboardControl.as_view(), name='indexControl'),
    # CONTROL DE VISITAS
    path('crear-visita/', crearControlVisitas.as_view(), name='crearVisita'),
    path('editar-visita/<int:pk>/', editarControlVisitas.as_view(), name='editarVisita'),
    # CONTROL DE REPORTES
    path('crear-reporte/', crearControlReportes.as_view(), name='crearReporte' ),
    path('editar-reporte/<int:pk>', editarControlReportes.as_view(), name='editarReporte'),
    # CONTROL DE PRESUPUESTOS
    path('presupuestos/', presupuestos.as_view(), name='presupuestos'),
    path('eliminar-presupuesto/<int:id>', eliminarPresupuesto, name='eliminarPresupuesto'),
    path('editar-presupuesto/<int:pk>', actualizarPresupuesto.as_view(), name='editarPresupuesto'),
    path('crear-presupuesto/', crearPresupuesto.as_view(), name='crearPresupuesto'),
    path('eliminar-presupuesto-tabla/<int:id>', eliminarPresupuestoTabla, name='eliminarPresupuestoTabla')
]