document.addEventListener("DOMContentLoaded", function () {
    const contenedor = document.getElementById("carrousel-contenedor");
    const wrapper = document.querySelector(".carrousel-reseñas");

    // Duplicamos las reseñas para que el scroll sea infinito
    contenedor.innerHTML += contenedor.innerHTML;

    let position = 0;
    let pausado = false;

    function animar() {
        if (!pausado) {
            position -= 0.5;
            if (Math.abs(position) >= contenedor.scrollWidth / 2) {
                position = 0;
            }
            contenedor.style.transform = `translateX(${position}px)`;
    }
        requestAnimationFrame(animar);
    }

    wrapper.addEventListener("mouseenter", () => pausado = true);
    wrapper.addEventListener("mouseleave", () => pausado = false);

    animar();
});