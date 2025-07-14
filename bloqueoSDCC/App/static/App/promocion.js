document.addEventListener('DOMContentLoaded', function () {
    const cartel = document.querySelector('.cartel-descuento');

    if (!cartel) return;

    const hoy = new Date();
    const fechaLimite = new Date('2025-08-30'); // 30 de agosto 2025

    // Verificar si estamos dentro del rango de fecha
    if (hoy <= fechaLimite) {
        cartel.style.display = 'block';
        localStorage.setItem('ultimaPromocion', hoy.toISOString());
    } else {
        const ultima = localStorage.getItem('ultimaPromocion');
        const ultimaFecha = ultima ? new Date(ultima) : null;

        // Mostrar de nuevo si pasaron 5 meses desde la última visualización
        if (
            !ultimaFecha ||
            hoy.getFullYear() > ultimaFecha.getFullYear() ||
            (hoy.getMonth() - ultimaFecha.getMonth() + 12) % 12 >= 5
        ) {
            cartel.style.display = 'block';
            localStorage.setItem('ultimaPromocion', hoy.toISOString());
        } else {
            cartel.style.display = 'none';
        }
    }
});