function enviarMensaje() {
    const mensajeInput = document.getElementById("mensajeInput");
    const mensaje = mensajeInput.value.trim();

    if (mensaje !== "") {
        agregarMensaje(mensaje);
        mensajeInput.value = "";
    }
}

function agregarMensaje(mensaje) {
    const chatBox = document.getElementById("chatBox");
    const nuevoMensaje = document.createElement("p");
    nuevoMensaje.textContent = mensaje;
    chatBox.appendChild(nuevoMensaje);
    chatBox.scrollTop = chatBox.scrollHeight;
}
