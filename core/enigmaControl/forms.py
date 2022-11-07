from django import forms
from core.enigmaVentas.models import MantenimientoClientes
from core.enigmaControl.models import PresupuestoTabla, controlVisitas, reportesControl, PresupuestoModelo

class controlVisitaForm(forms.ModelForm):

    class Meta:
        model = controlVisitas
        exclude = ['usuario']
        fields = '__all__'


class controlReportesForm(forms.ModelForm):

    class Meta:
        model = reportesControl
        exclude = ['usuario']
        fields = '__all__'

class presupuestoForm(forms.ModelForm):

    class Meta:
        model = PresupuestoModelo
        exclude = ['usuario']
        fields = '__all__'






class presupuestoTablaForm(forms.ModelForm):
    
    class Meta:
        model = PresupuestoTabla
        exclude = ['usuario']
        fields = '__all__'