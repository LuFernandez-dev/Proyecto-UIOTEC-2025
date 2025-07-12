from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User

#Decorador
def solo_superusuario(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

#Crea tus vistas aqui

#Home
def mostrar_home(request):
    enviado = False
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save()
            enviado = True
            form = ContactoForm()

            # --- Email al cliente (HTML) ---
            asunto_cliente = '¡Gracias por contactarte con SDCC!'
            texto_cliente = f'Hola {contacto.nombre}, gracias por tu mensaje.'
            html_cliente = render_to_string('App/confirmacion_contacto.html', {'contacto': contacto})

            email_cliente = EmailMultiAlternatives(
                asunto_cliente,
                texto_cliente,
                'sdcc@tudominio.com',
                [contacto.email],
            )
            email_cliente.attach_alternative(html_cliente, "text/html")
            email_cliente.send()

            # --- Email al superusuario con los datos del cliente (HTML) ---
            superusers = User.objects.filter(is_superuser=True)
            for admin in superusers:
                asunto_admin = '📥 Nuevo contacto recibido'
                texto_admin = 'Nuevo cliente interesado en SDCC'
                html_admin = render_to_string('App/superuser_notificacion.html', {'contacto': contacto})

                email_admin = EmailMultiAlternatives(
                    asunto_admin,
                    texto_admin,
                    'sdcc@tudominio.com',
                    [admin.email],
                )
                email_admin.attach_alternative(html_admin, "text/html")
                email_admin.send()
    else:
        form = ContactoForm()

    return render(request, 'App/home.html', {'form': form, 'enviado': enviado})

#Login del superuser
def superuser_login_view(request):
    if request.method == 'POST':
        form = SuperUserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Datos incorrectos.')
    else:
        form = SuperUserLoginForm()
    return render(request, 'App/login.html', {'form': form})

#Cerrar seccion del superuser
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

#Soporte tecnico
def soporte_tecnico(request):
    return render(request, 'App/soporte_tecnico.html')

#Instalaciones
#Lista de instalaciones
@solo_superusuario
def instalacion_list(request):
    instalaciones = Instalacion.objects.all()
    return render(request, 'App/instalacion_list.html', {'instalaciones': instalaciones})

#Crear instalación
@solo_superusuario
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
@solo_superusuario
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
@solo_superusuario
def eliminar_instalacion(request, pk):
    instalacion = get_object_or_404(Instalacion, pk=pk)
    if request.method == 'POST':
        instalacion.delete()
        return redirect('instalacion_list')
    return render(request, 'App/instalacion_confirm_delete.html', {'object': instalacion})

#Tecnico
#Lista de tecnicos
@solo_superusuario
def tecnico_list(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'App/tecnico_list.html', {'tecnicos': tecnicos})

#Registra tecnico
@solo_superusuario
def crear_tecnico(request):
    form = TecnicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tecnico_list')
    return render(request, 'App/tecnico_form.html', {'form': form})

#Editar tecnico
@solo_superusuario
def editar_tecnico(request, pk):
    tecnico = get_object_or_404(Tecnico, pk=pk)
    form = TecnicoForm(request.POST or None, instance=tecnico)
    if form.is_valid():
        form.save()
        return redirect('tecnico_list')
    return render(request, 'App/tecnico_form.html', {'form': form})

#Elimina tecnico
@solo_superusuario
def eliminar_tecnico(request, pk):
    tecnico = get_object_or_404(Tecnico, pk=pk)
    if request.method == 'POST':
        tecnico.delete()
        return redirect('tecnico_list')
    return render(request, 'App/tecnico_confirm_delete.html', {'object': tecnico})

#Venta
#Lista de venta
@solo_superusuario
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'App/venta_list.html', {'ventas': ventas})

#Registra venta
@solo_superusuario
def crear_venta(request):
    form = VentaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('venta_list')
    return render(request, 'App/venta_form.html', {'form': form})

#Edita venta
@solo_superusuario
def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    form = VentaForm(request.POST or None, instance=venta)
    if form.is_valid():
        form.save()
        return redirect('venta_list')
    return render(request, 'App/venta_form.html', {'form': form})

#Elimina venta
@solo_superusuario
def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('venta_list')
    return render(request, 'App/venta_confirm_delete.html', {'object': venta})

#Contacto
#Lista de contacto
@solo_superusuario
def contacto_list(request):
    contactos = Contacto.objects.all()

    dni = request.GET.get('dni')
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    email = request.GET.get('email')
    telefono = request.GET.get('telefono')

    if dni:
        contactos = contactos.filter(dni__icontains=dni)
    if nombre:
        contactos = contactos.filter(nombre__icontains=nombre)
    if apellido:
        contactos = contactos.filter(apellido__icontains=apellido)
    if email:
        contactos = contactos.filter(email__icontains=email)
    if telefono:
        contactos = contactos.filter(telefono__icontains=telefono)

    context = {
        'contactos': contactos,
        'filtros': {
            'dni': dni or '',
            'nombre': nombre or '',
            'apellido': apellido or '',
            'email': email or '',
            'telefono': telefono or '',
        }
    }
    return render(request, 'App/contacto_list.html', context)

#Edita contacto
@solo_superusuario
def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    form = ContactoForm(request.POST or None, instance=contacto)
    if form.is_valid():
        form.save()
        return redirect('contacto_list')
    return render(request, 'App/contacto_form.html', {'form': form})

#Elimina venta
@solo_superusuario
def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('contacto_list')
    return render(request, 'App/contacto_confirm_delete.html', {'object': contacto})

#VersionProducto
#Lista de version de producto
@solo_superusuario
def versionproducto_list(request):
    versiones = VersionProducto.objects.all()
    return render(request, 'App/versionproducto_list.html', {'versiones': versiones})

#Registrar version del producto
@solo_superusuario
def crear_versionproducto(request):
    form = VersionProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('versionproducto_list')
    return render(request, 'App/versionproducto_form.html', {'form': form})

#Editar version del producto
@solo_superusuario
def editar_versionproducto(request, pk):
    version = get_object_or_404(VersionProducto, pk=pk)
    form = VersionProductoForm(request.POST or None, instance=version)
    if form.is_valid():
        form.save()
        return redirect('versionproducto_list')
    return render(request, 'App/versionproducto_form.html', {'form': form})

#Eliminar version del producto
@solo_superusuario
def eliminar_versionproducto(request, pk):
    version = get_object_or_404(VersionProducto, pk=pk)
    if request.method == 'POST':
        version.delete()
        return redirect('versionproducto_list')
    return render(request, 'App/versionproducto_confirm_delete.html', {'object': version})

#Términos y Condiciones
def terminos(request):
    return render(request, 'App/terminos.html')

#Política de Privacidad
def privacidad(request):
    return render(request, 'App/privacidad.html')
