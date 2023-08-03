function suma(nroUno, nroDos) {
    return parseInt(nroUno) + parseInt(nroDos)
}

document.getElementById("miForm").addEventListener("submit", function (evento) {
        evento.preventDefault();

        let numeroUno = document.getElementById("nroUno").value;
        let numeroDos = document.getElementById("nroDos").value;

        let sum = suma(numeroUno, numeroDos);
        console.log(`${sum}`)

        const divVisor = document.getElementById("visor") 
        divVisor.innerText = `${sum}`
    }
)