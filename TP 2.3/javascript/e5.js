// Escribe una función que tome un número como parámetro y calcule la suma de todos los números primos menores o iguales a ese número.
function cribaEratostenes(n) {
    let listaNumeros = []
    for (let i = 2; i <= n; i++) {
        for (let j = i+1; j <= n; j++) {
            if (j % i == 0 && !listaNumeros.includes(j)) {
                listaNumeros.push(j);
            }
        }
    }
    return sumaPrimo(listaNumeros, n);
}

function sumaPrimo(listaNum, n) {
    let total = 0;
    for (let i = 2; i <= n; i++) {
        if (!listaNum.includes(i)) {
            total += i;
        }
    }
    return total;
}

document.getElementById("divForm").addEventListener("submit", function (evento) {
    evento.preventDefault();

    let n = document.getElementById("numero").value;
    
    let sum = cribaEratostenes(parseInt(n));
    console.log(`Suma de primos: ${sum}`)
    
    let visor = document.getElementById("visor");
    visor.innerText = `Suma de primos: ${sum}`
})
