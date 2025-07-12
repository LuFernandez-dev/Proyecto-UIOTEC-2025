document.addEventListener('DOMContentLoaded', function () {
    const mensaje = document.getElementById('mensaje');

    if (mensaje) {
        // Agregar la animación de entrada
        mensaje.classList.add('mensaje-animar-entrada');

        // Después de 4 segundos, iniciar la salida
        setTimeout(() => {
            mensaje.classList.remove('mensaje-animar-entrada'); // evitar conflicto
            mensaje.classList.add('mensaje-animar-salida');

            // Remover el mensaje después de la animación de salida
            setTimeout(() => mensaje.remove(), 600); // esperar 0.6s
        }, 4000);
    }
});