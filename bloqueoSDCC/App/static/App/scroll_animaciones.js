function mostrarAnimacionScroll() {
    var elementos = document.querySelectorAll('.animacion-img, .animacion-scroll');
    var windowHeight = window.innerHeight;

    elementos.forEach(function(el) {
        var posicion = el.getBoundingClientRect().top;
        var alturaElemento = el.offsetHeight;

        if (posicion < windowHeight - 40 && posicion + alturaElemento > 40) {
            el.classList.add('visible');
        } else {
            el.classList.remove('visible');
        }
    });
}

window.addEventListener('scroll', mostrarAnimacionScroll);
window.addEventListener('resize', mostrarAnimacionScroll);
window.addEventListener('DOMContentLoaded', mostrarAnimacionScroll);
document.addEventListener('touchmove', mostrarAnimacionScroll);
document.addEventListener('wheel', mostrarAnimacionScroll);