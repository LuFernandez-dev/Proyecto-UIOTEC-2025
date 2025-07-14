document.addEventListener('DOMContentLoaded', function () {
    const btnHamburguesa = document.getElementById('hamburger-btn');
    const menuNav = document.querySelector('nav');

    if (btnHamburguesa && menuNav) {
        btnHamburguesa.addEventListener('click', function () {
            menuNav.classList.toggle('mostrar-menu');
        });
    }
});