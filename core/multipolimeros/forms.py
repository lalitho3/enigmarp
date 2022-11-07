from django import forms
from django.forms import ModelForm
from .models import MantenimientoPMultiP, MantenimientoClientes, SolicitudCredito


class MantenimientoMultiPForm(ModelForm):


    class Meta:
        model = MantenimientoPMultiP
        exclude = ['Usuario']
        fields = ('__all__')


class MantenimientoClientesForm(ModelForm):


    class Meta:
        model = MantenimientoClientes
        exclude = ['Usuario']
        fields = ('__all__')


class CreditoForm(ModelForm):

   

    class Meta:
        model = SolicitudCredito
        exclude = ['Usuario']
        fields = ('__all__')
        widgets={
            'DocumentosEntregados': forms.CheckboxSelectMultiple(attrs={'class':'form-control col-lg-12'}),
        }