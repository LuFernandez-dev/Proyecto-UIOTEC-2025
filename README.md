# S.D.C.C. - Sistema de Cierre Centralizado

Proyecto desarrollado en Django para la gestión de clientes, instalaciones y ventas del sistema S.D.C.C., un innovador sistema de seguridad para vehículos que refuerza el cierre de puertas desde el parante B, activado vía Bluetooth o control remoto.

## Características principales
- Registro y gestión de clientes, técnicos, instalaciones y ventas.
- Panel de administración para superusuarios.
- Envío automático de emails de confirmación y notificación.
- Formularios web para contacto y solicitud de instalación.
- Promociones y comunicación de beneficios desde la web.

## ¿Cómo funciona S.D.C.C.?
El sistema S.D.C.C. refuerza el cierre de las puertas desde el interior del auto, actuando sobre el parante B mediante un mecanismo robusto y discreto. Se activa vía Bluetooth desde el celular o control remoto, sin contacto físico. Una placa Arduino comanda el servomotor que bloquea la puerta en segundos. Funciona con batería recargable, es adaptable a distintos modelos y no altera el diseño del vehículo.

## Instalación y uso
1. Clona este repositorio.
2. Activa el entorno virtual:
   powershell
   cd bloqueoSDCC
   ..\entorno\Scripts\activate
   
3. Instala las dependencias:
   powershell
   pip install django
   
4. Realiza las migraciones:
   powershell
   python manage.py migrate
   
5. Ejecuta el servidor de desarrollo:
   powershell
   python manage.py runserver
   
6. Accede a la app en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Vistas de la aplicación

La app cuenta con dos partes diferenciadas según el tipo de usuario:

- *Vista para clientes:*
  - Es la página principal ("home") a la que accede cualquier visitante.
  - Permite conocer el producto, ver promociones, solicitar información y enviar datos de contacto mediante formularios.
  - El cliente no necesita registrarse ni autenticarse.

- *Vista para superusuario:*
  - Acceso restringido mediante login de superusuario.
  - Permite gestionar (CRUD) los datos de clientes, instalaciones, técnicos, ventas y versiones del producto desde un panel administrativo.
  - El superusuario recibe notificaciones por email cuando un cliente envía un formulario.
  - Solo los superusuarios pueden acceder a estas funciones avanzadas.

## Modelos principales
- *Contacto*: Datos de clientes.
- *VersionProducto*: Versiones y descripciones del producto.
- *Instalacion*: Gestión de instalaciones y su estado.
- *Tecnico*: Técnicos responsables de instalaciones.
- *Venta*: Registro de ventas y métodos de pago.

## Estructura del proyecto
- App/: Lógica principal, modelos, vistas y formularios.
- static/App/: Archivos estáticos (JS, CSS, imágenes).
- Templates/App/: Plantillas HTML.
- entorno/: Entorno virtual de Python.

## Créditos
Desarrollado por Martin Avalos, Lucas Fernandez, Marina Astrada, Celeste Mancini, Gabriela Moya Vega.


¡Contribuciones y sugerencias son bienvenidas!
