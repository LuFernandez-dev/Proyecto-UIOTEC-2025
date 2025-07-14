document.addEventListener('DOMContentLoaded', function () {
    const btnHamburguesa = document.getElementById('hamburger-btn');
    const nav = document.querySelector('header nav');

    if (btnHamburguesa && nav) {
        btnHamburguesa.addEventListener('click', function () {
            nav.classList.toggle('mostrar-menu');
        });
    }
});