from django import forms
from core.enigmaVentas.models import *


class mantenimientoProspectosForm(forms.ModelForm):
    class Meta:
        model = MantenimientoProspectos
        exclude = ['Usuario']
        fields = '__all__'


class mantenimiendoClientesForm(forms.ModelForm):
    class Meta:
        model = MantenimientoClientes
        exclude = ['Usuario']
        fields = '__all__'


class solicitudCreditoForm(forms.ModelForm):
    class Meta:
        model = SolicitudCredito
        exclude = ['Usuario']
        fields = '__all__'
        widgets={
            'DocumentosEntregados': forms.CheckboxSelectMultiple(attrs={'class':'form-control col-lg-12'}),
        }
