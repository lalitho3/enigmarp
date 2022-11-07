from django.urls import path
from core.enigmaAdmin.views import *

app_name = 'enigmaAdmin'


urlpatterns = [
    path('', dashboardAdmin.as_view(), name='dashboardAdmin'),
    path('personal/<int:pk>/', gestionPersonal.as_view(), name='gestionPersonal'),
    path('presupuestos/', administrarPresupuestos.as_view(), name='administrarPresupuestos'),
    path('presupuestos/<int:pk>/', tablaPresupuestos.as_view(), name='tablaPresupuestos'),
]