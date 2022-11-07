from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.enigmaControl.views import presupuestosViewSet, usuariosViewSet
from system import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'usuarios', usuariosViewSet)
router.register(r'presupuestos', presupuestosViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.enigma.urls')),
    # URLS DE ENIGMA
    path('erp/', include('core.enigmaErp.urls')),
    path('control/', include('core.enigmaControl.urls')),
    path('ventas/', include('core.enigmaVentas.urls')),
    path('administracion/', include('core.enigmaAdmin.urls')),\
    # URLS DE MULTIPOLIMEROS
    path('multipolimeros/', include('core.multipolimeros.urls')),
    # URLS DE TERCEROS
    path('accounts/', (include(('django.contrib.auth.urls', 'auth'), namespace='auth' ))),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)), 
]

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


