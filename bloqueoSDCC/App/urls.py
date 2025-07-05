from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', mostrar_home, name='home'),
    path('contactos/', contacto_list, name='contacto_list'),
    path('contactos/nuevo/', ContactoCreateView.as_view(), name='contacto_create'),
    path('contactos/editar/<int:pk>/', ContactoUpdateView.as_view(), name='contacto_update'),
    path('contactos/eliminar/<int:pk>/', ContactoDeleteView.as_view(), name='contacto_delete'),
    path('versiones/', versionproducto_list, name='versionproducto_list'),
    path('versiones/nueva/', VersionProductoCreateView.as_view(), name='versionproducto_create'),
    path('versiones/editar/<int:pk>/', VersionProductoUpdateView.as_view(), name='versionproducto_update'),
    path('versiones/eliminar/<int:pk>/', VersionProductoDeleteView.as_view(), name='versionproducto_delete'),
    path('instalaciones/', instalacion_list, name='instalacion_list'),
    path('instalaciones/nueva/', InstalacionCreateView.as_view(), name='instalacion_create'),
    path('instalaciones/editar/<int:pk>/', InstalacionUpdateView.as_view(), name='instalacion_update'),
    path('instalaciones/eliminar/<int:pk>/', InstalacionDeleteView.as_view(), name='instalacion_delete'),
    path('ventas/', venta_list, name='venta_list'),
    path('ventas/nueva/', VentaCreateView.as_view(), name='venta_create'),
    path('ventas/editar/<int:pk>/', VentaUpdateView.as_view(), name='venta_update'),
    path('ventas/eliminar/<int:pk>/', VentaDeleteView.as_view(), name='venta_delete'),
    path('tecnicos/', tecnico_list, name='tecnico_list'),
    path('tecnicos/nuevo/', TecnicoCreateView.as_view(), name='tecnico_create'),
    path('tecnicos/editar/<int:pk>/', TecnicoUpdateView.as_view(), name='tecnico_update'),
    path('tecnicos/eliminar/<int:pk>/', TecnicoDeleteView.as_view(), name='tecnico_delete'),
]