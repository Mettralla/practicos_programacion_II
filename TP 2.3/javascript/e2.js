function ordenAsc(numArray) {
    for (let i = 0; i < numArray.length; i++) {
        for (let j = 0; j < numArray.length; j++) {
            if (parseInt(numArray[j]) > parseInt(numArray[j + 1])) {
                let temp = numArray[j];
                numArray[j] = numArray[j + 1];
                numArray[j + 1] = temp;
            }
        }
    }
    return numArray
}

document.getElementById("ArrayForm").addEventListener("submit",
function (evento) {
    evento.preventDefault();

    let arrayDesordenado = document.getElementById("arrayDesordenado").value;

    let arrayOrdenado = ordenAsc(arrayDesordenado.split(",").map(item => item.trim()));

    console.log(`Lista ordenada: ${arrayOrdenado}`)

    const visor = document.getElementById("visor");
    visor.innerText = `Lista ordenada: ${arrayOrdenado}`
})
