function filtrarPares(numArray) {
    return numArray.filter(item => item % 2 != 0);
}

let lista = [2,1,3,9,7,4,8,2,11,5];

const preFiltro = document.getElementById("vector");
preFiltro.innerText = `Sin Filtro: ${lista}`

let listaFiltrada = filtrarPares(lista)
console.log(`Filtro Pares: ${listaFiltrada}`)

const visor = document.getElementById("visor");
visor.innerText = `Filtro Pares: ${listaFiltrada}`
