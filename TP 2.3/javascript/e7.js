function visibilidadDiv() {
    const div = document.getElementById("miDiv");
    const btn = document.getElementById("btn");
    if (div.style.display === "none") {
        div.style.display = "block";
        btn.innerText = "Ocultar"
    } else {
        div.style.display = "none";
        btn.innerText = "Mostrar"
    }
}