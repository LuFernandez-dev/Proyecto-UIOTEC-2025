from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', mostrar_home, name='home'),
    path('contactos/', contacto_list, name='contacto_list'),
    path('contactos/editar/<int:pk>/', editar_contacto, name='contacto_update'),
    path('contactos/eliminar/<int:pk>/', eliminar_contacto, name='contacto_delete'),
    path('versiones/', versionproducto_list, name='versionproducto_list'),
    path('versiones/nueva/', crear_versionproducto, name='versionproducto_create'),
    path('versiones/editar/<int:pk>/', editar_versionproducto, name='versionproducto_update'),
    path('versiones/eliminar/<int:pk>/', eliminar_versionproducto, name='versionproducto_delete'),
    path('instalaciones/', instalacion_list, name='instalacion_list'),
    path('instalaciones/nueva/', crear_instalacion, name='instalacion_create'),
    path('instalaciones/editar/<int:pk>/', editar_instalacion, name='instalacion_update'),
    path('instalaciones/eliminar/<int:pk>/', eliminar_instalacion, name='instalacion_delete'),
    path('ventas/', venta_list, name='venta_list'),
    path('ventas/nueva/', crear_venta, name='venta_create'),
    path('ventas/editar/<int:pk>/', editar_venta, name='venta_update'),
    path('ventas/eliminar/<int:pk>/', eliminar_venta, name='venta_delete'),
    path('tecnicos/', tecnico_list, name='tecnico_list'),
    path('tecnicos/nuevo/', crear_tecnico, name='tecnico_create'),
    path('tecnicos/editar/<int:pk>/', editar_tecnico, name='tecnico_update'),
    path('tecnicos/eliminar/<int:pk>/', eliminar_tecnico, name='tecnico_delete'),
    path('login/', superuser_login_view, name='superuser_login'),
    path('logout/', cerrar_sesion, name='cerrar_sesion'),
    path('terminos/', terminos, name='terminos'),
    path('privacidad/', privacidad, name='privacidad'),
    path('soporte/', soporte_tecnico, name='soporte_tecnico'),
    path('mas-informacion/', mas_informacion, name='mas_informacion'),
] 
