document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('modal-img');
    const modalImg = document.getElementById('img-grande');
    const modalTexto = document.getElementById('texto-grande');
    const cerrar = document.querySelector('.cerrar');

    document.querySelectorAll('.img-click').forEach(img => {
        img.addEventListener('click', () => {
            modal.style.display = "flex";
            modalImg.src = img.dataset.img;

            // Buscar el figcaption del mismo figure
            const figcaption = img.parentElement.querySelector('figcaption');
            modalTexto.textContent = figcaption ? figcaption.textContent : '';
        });
    });

    cerrar.addEventListener('click', () => {
        modal.style.display = "none";
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });
});