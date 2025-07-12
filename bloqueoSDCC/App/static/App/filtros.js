document.addEventListener("DOMContentLoaded", function() {
    const btnToggle = document.getElementById("btnToggleFiltros");
    const formFiltros = document.querySelector(".formulario-filtros");

    if (btnToggle && formFiltros) {
        btnToggle.addEventListener("click", () => {
            formFiltros.classList.toggle("oculto");
        });
    }
});