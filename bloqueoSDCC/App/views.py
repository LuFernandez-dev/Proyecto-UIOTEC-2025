from django.shortcuts import render
from django.views.generic import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

#Crea tus vistas aqui
#Home
def mostrar_home(request):
    return render(request, 'App/home.html')

#Instalaciones
#Lista de instalaciones
def instalacion_list(request):
    instalaciones = Instalacion.objects.all()
    return render(request, 'App/instalacion_list.html', {'instalaciones': instalaciones})

#Crea instalación
class InstalacionCreateView(CreateView):
    model = Instalacion
    template_name = 'App/instalacion_form.html'
    form_class = InstalacionForm
    success_url = reverse_lazy('instalacion_list')

#Editar instalación
class InstalacionUpdateView(UpdateView):
    model = Instalacion
    template_name = 'App/instalacion_form.html'
    form_class = InstalacionForm
    success_url = reverse_lazy('instalacion_list')

#Eliminar instalación
class InstalacionDeleteView(DeleteView):
    model = Instalacion
    template_name = 'App/instalacion_confirm_delete.html'
    success_url = reverse_lazy('instalacion_list')

#Tecnico
#Lista de tecnicos
def tecnico_list(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'App/tecnico_list.html', {'tecnicos': tecnicos})

#Crear técnico
class TecnicoCreateView(CreateView):
    model = Tecnico
    template_name = 'App/tecnico_form.html'
    form_class = TecnicoForm
    success_url = reverse_lazy('tecnico_list')

#Editar técnico
class TecnicoUpdateView(UpdateView):
    model = Tecnico
    template_name = 'App/tecnico_form.html'
    form_class = TecnicoForm
    success_url = reverse_lazy('tecnico_list')

#Eliminar técnico
class TecnicoDeleteView(DeleteView):
    model = Tecnico
    template_name = 'App/tecnico_confirm_delete.html'
    success_url = reverse_lazy('tecnico_list')

#Venta
#Lista de venta
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'App/venta_list.html', {'ventas': ventas})

#Nueva Venta
class VentaCreateView(CreateView):
    model = Venta
    template_name = 'App/venta_form.html'
    form_class = VentaForm
    success_url = reverse_lazy('venta_list')

#Editar Venta
class VentaUpdateView(UpdateView):
    model = Venta
    template_name = 'App/venta_form.html'
    form_class = VentaForm
    success_url = reverse_lazy('venta_list')

#Eliminar Venta
class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'App/venta_confirm_delete.html'
    success_url = reverse_lazy('venta_list')

#Contacto
#Lista de contacto
def contacto_list(request):
    contactos = Contacto.objects.all()
    return render(request, 'App/contacto_list.html', {'contactos': contactos})

#Crear contacto
class ContactoCreateView(CreateView):   
    model = Contacto
    template_name = 'App/contacto_form.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto_list') 

#Editar contacto
class ContactoUpdateView(UpdateView):
    model = Contacto
    template_name = 'App/contacto_form.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto_list')

# Eliminar contacto
class ContactoDeleteView(DeleteView):
    model = Contacto
    template_name = 'App/contacto_confirm_delete.html'
    success_url = reverse_lazy('contacto_list')

#VersionProducto
#Lista de version de producto
def versionproducto_list(request):
    versiones = VersionProducto.objects.all()
    return render(request, 'App/versionproducto_list.html', {'versiones': versiones})

#Nueva VersionProducto
class VersionProductoCreateView(CreateView):
    model = VersionProducto
    template_name = 'App/versionproducto_form.html'
    form_class = VersionProductoForm
    success_url = reverse_lazy('versionproducto_list')

#Editar VersionProducto
class VersionProductoUpdateView(UpdateView):
    model = VersionProducto
    template_name = 'App/versionproducto_form.html'
    form_class = VersionProductoForm
    success_url = reverse_lazy('versionproducto_list')

#Eliminar VersionProducto
class VersionProductoDeleteView(DeleteView):
    model = VersionProducto
    template_name = 'App/versionproducto_confirm_delete.html'
    success_url = reverse_lazy('versionproducto_list')