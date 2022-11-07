from django.urls import path
from core.enigma.views import indexView

app_name = 'enigma'

urlpatterns = [
    path('', indexView.as_view(), name='index'),
]