from django.db import models

#Crea tus modelos aqui
class Contacto(models.Model):
    dni = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.dni} - {self.nombre} - {self.apellido} - {self.email} - {self.telefono}"

class VersionProducto(models.Model):
    nombre = models.CharField(max_length=35)
    descripcion = models.TextField(max_length = 600)
    fecha_lanzamiento = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.fecha_lanzamiento}"

class Instalacion(models.Model):
    
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Completado', 'Completado'),
    ]

    cliente = models.ForeignKey('Contacto', on_delete=models.CASCADE)
    vehiculo = models.CharField(max_length=25)
    direccion = models.CharField(max_length=50)
    fecha_instalacion = models.DateTimeField()
    estado = models.CharField(choices=ESTADOS)
    notas = models.TextField(blank=True, null=True, max_length = 600)

    def __str__(self):
        return f"{self.cliente.dni} - {self.cliente.nombre} - {self.cliente.apellido} - {self.vehiculo} - {self.direccion} - {self.fecha_instalacion} - {self.estado} - {self.notas}"


class Tecnico(models.Model):
    legajo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.legajo} - {self.nombre} - {self.apellido} - {self.telefono}"

class Venta(models.Model):
    METODO = [
        ('Debito', 'Debito'),
        ('Credito', 'Credito'),
        ('Tranferencia', 'Tranferencia'),
    ]

    cliente = models.ForeignKey('Contacto', on_delete=models.CASCADE)
    forma_pago = models.CharField(choices=METODO)
    importe = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_compra = models.DateTimeField()

    def __str__(self):
        return f"{self.cliente.dni} - {self.forma_pago} - {self.importe} - {self.fecha_compra}"