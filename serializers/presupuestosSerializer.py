from rest_framework import serializers
from core.enigmaControl.models import PresupuestoTabla
from django.contrib.auth.models import User

class PresupuestoTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresupuestoTabla
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):

    usuarioPresupuestos = PresupuestoTablaSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'usuarioPresupuestos']