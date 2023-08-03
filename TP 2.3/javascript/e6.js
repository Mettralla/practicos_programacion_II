const boton = document.getElementById("btn");
let esVerde = true;

function cambiarColor() {
    esVerde = !esVerde;
    boton.style.backgroundColor = esVerde ? "green" : "red" ;
}

boton.addEventListener("click", cambiarColor);

