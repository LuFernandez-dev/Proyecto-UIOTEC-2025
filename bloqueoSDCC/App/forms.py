from django import forms
from .models import *

#Formulario para Contacto
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['dni', 'nombre', 'apellido', 'email', 'telefono']

#Formulario para VersionProducto
class VersionProductoForm(forms.ModelForm):
    class Meta:
        model = VersionProducto
        fields = ['nombre', 'descripcion', 'fecha_lanzamiento']
        widgets = {
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'nombre': 'Nombre de version',
            'fecha_lanzamiento': 'Fecha de lanzamiento',
        }

#Formulario para Instalacion
class InstalacionForm(forms.ModelForm):
    class Meta:
        model = Instalacion
        fields = ['cliente', 'vehiculo', 'direccion', 'fecha_instalacion', 'estado', 'notas']
        widgets = {
            'fecha_instalacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'fecha_instalacion': 'Fecha de instalación',
            'notas': 'Observaciones adicionales',
        }

#Formulario para Tecnico
class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['legajo', 'nombre', 'apellido', 'telefono']

#Formulario para Venta
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'forma_pago', 'importe', 'fecha_compra']
        widgets = {
            'fecha_compra': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'forma_pago': 'Forma de pago',
            'fecha_compra': 'Fecha de compra'
        }

#Formulario del login del superuser
class SuperUserLoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=150)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)