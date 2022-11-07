from django.urls import path 
from core.enigmaErp.views import dashboardView

app_name = 'enigmaErp'

urlpatterns = [
    path('', dashboardView.as_view(), name='dashboard'),
]