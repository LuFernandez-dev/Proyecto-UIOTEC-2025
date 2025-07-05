from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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

#Crear instalación
def crear_instalacion(request):
    if request.method == 'POST':
        form = InstalacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instalacion_list')
    else:
        form = InstalacionForm()
    return render(request, 'App/instalacion_form.html', {'form': form})

#Editar instalación
def editar_instalacion(request, pk):
    instalacion = get_object_or_404(Instalacion, pk=pk)
    if request.method == 'POST':
        form = InstalacionForm(request.POST, instance=instalacion)
        if form.is_valid():
            form.save()
            return redirect('instalacion_list')
    else:
        form = InstalacionForm(instance=instalacion)
    return render(request, 'App/instalacion_form.html', {'form': form})

#Eliminar instalación
def eliminar_instalacion(request, pk):
    instalacion = get_object_or_404(Instalacion, pk=pk)
    if request.method == 'POST':
        instalacion.delete()
        return redirect('instalacion_list')
    return render(request, 'App/instalacion_confirm_delete.html', {'object': instalacion})

#Tecnico
#Lista de tecnicos
def tecnico_list(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'App/tecnico_list.html', {'tecnicos': tecnicos})

#Registra tecnico
def crear_tecnico(request):
    form = TecnicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tecnico_list')
    return render(request, 'App/tecnico_form.html', {'form': form})

#Editar tecnico
def editar_tecnico(request, pk):
    tecnico = get_object_or_404(Tecnico, pk=pk)
    form = TecnicoForm(request.POST or None, instance=tecnico)
    if form.is_valid():
        form.save()
        return redirect('tecnico_list')
    return render(request, 'App/tecnico_form.html', {'form': form})

#Elimina tecnico
def eliminar_tecnico(request, pk):
    tecnico = get_object_or_404(Tecnico, pk=pk)
    if request.method == 'POST':
        tecnico.delete()
        return redirect('tecnico_list')
    return render(request, 'App/tecnico_confirm_delete.html', {'object': tecnico})

#Venta
#Lista de venta
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'App/venta_list.html', {'ventas': ventas})

#Registra venta
def crear_venta(request):
    form = VentaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('venta_list')
    return render(request, 'App/venta_form.html', {'form': form})

#Edita venta
def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    form = VentaForm(request.POST or None, instance=venta)
    if form.is_valid():
        form.save()
        return redirect('venta_list')
    return render(request, 'App/venta_form.html', {'form': form})

#Elimina venta
def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('venta_list')
    return render(request, 'App/venta_confirm_delete.html', {'object': venta})

#Contacto
#Lista de contacto
def contacto_list(request):
    contactos = Contacto.objects.all()
    return render(request, 'App/contacto_list.html', {'contactos': contactos})

#Registra contacto
def crear_contacto(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contacto_list')
    return render(request, 'App/contacto_form.html', {'form': form})

#Edita contacto
def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    form = ContactoForm(request.POST or None, instance=contacto)
    if form.is_valid():
        form.save()
        return redirect('contacto_list')
    return render(request, 'App/contacto_form.html', {'form': form})

#Elimina venta
def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('contacto_list')
    return render(request, 'App/contacto_confirm_delete.html', {'object': contacto})

#VersionProducto
#Lista de version de producto
def versionproducto_list(request):
    versiones = VersionProducto.objects.all()
    return render(request, 'App/versionproducto_list.html', {'versiones': versiones})

#Registrar version del producto
def crear_versionproducto(request):
    form = VersionProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('versionproducto_list')
    return render(request, 'App/versionproducto_form.html', {'form': form})

#Editar version del producto
def editar_versionproducto(request, pk):
    version = get_object_or_404(VersionProducto, pk=pk)
    form = VersionProductoForm(request.POST or None, instance=version)
    if form.is_valid():
        form.save()
        return redirect('versionproducto_list')
    return render(request, 'App/versionproducto_form.html', {'form': form})

#Eliminar version del producto
def eliminar_versionproducto(request, pk):
    version = get_object_or_404(VersionProducto, pk=pk)
    if request.method == 'POST':
        version.delete()
        return redirect('versionproducto_list')
    return render(request, 'App/versionproducto_confirm_delete.html', {'object': version})