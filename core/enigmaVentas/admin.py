from django.contrib import admin
from core.enigmaVentas.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProductosResource(resources.ModelResource):
    class Meta:
        model = Productos


class ProductosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['descripcion']
    list_display = ('codLinea','codColor', 'descripcion', 'lpa', 'lpd')
    resource_class = ProductosResource


class ProspectosResource(resources.ModelResource):
    class Meta:
        model = MantenimientoProspectos

class ProspectosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['RazonSocial']
    list_display = ('RazonSocial', 'Rfc', 'NombreComercial', 'DireccionFiscal', 'CorreoElectronico', 'TelefonoCelular')
    resource_class = ProspectosResource

class ClientesResource(resources.ModelResource):
    class Meta:
        model = MantenimientoClientes

class ClientesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['RazonSocial']
    list_display = ('RazonSocial', 'Rfc', 'NombreComercial', 'DireccionFiscal', 'CorreoElectronico', 'TelefonoCelular')
    resource_class = ClientesResource

class CreditosResource(resources.ModelResource):
    class Meta:
        model = SolicitudCredito

class CreditosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['RazonSocial']
    list_display = ('RazonSocial', 'Rfc', 'NombreComercial', 'DireccionFiscal', 'CorreoElectronico', 'Telefono')
    resource_class = CreditosResource    


admin.site.register(Prospectos)
admin.site.register(MantenimientoProspectos, ProspectosAdmin)
admin.site.register(MantenimientoClientes, ClientesAdmin)
admin.site.register(SolicitudCredito, CreditosAdmin)
admin.site.register(Documentos)
admin.site.register(Productos, ProductosAdmin)
