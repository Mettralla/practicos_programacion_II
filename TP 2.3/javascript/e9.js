// Crear un documento HTML con un formulario que contenga los campos Nombre y Email, se pide recuperar los valores ingresados y mostrarlos por consola.

const formulario = document.getElementById("miForm");

formulario.addEventListener("submit", function(evento) {
    evento.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;

    console.log("Nombre:", nombre);
    console.log("Email:", email);
});