document.addEventListener('DOMContentLoaded', function () {
    const mensaje = document.getElementById('mensaje');

    if (mensaje) {
        // Animación de entrada
        mensaje.classList.add('mensaje-animar-entrada');

        // Salida luego de 4 segundos
        setTimeout(() => {
            mensaje.classList.remove('mensaje-animar-entrada');
            mensaje.classList.add('mensaje-animar-salida');
            setTimeout(() => mensaje.remove(), 600);
        }, 4000);
    }

    // Desplazar al formulario si hay errores
    if (mensaje && mensaje.classList.contains('mensaje-error')) {
        const formulario = document.getElementById('formulario-contacto');
        if (formulario) {
            formulario.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
});