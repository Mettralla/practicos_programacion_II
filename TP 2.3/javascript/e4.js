// Encontrar el número más grande en un Array.

function maxArray(numArray) {
    let maxNum = 0;
    numArray.forEach(num => {
        if (num > maxNum) {
            maxNum = num;
        }
    })
    return maxNum;
}

const numArray = [15, 7, 32, 11, 23, 6, 45];

let mayorNum = maxArray(numArray);

console.log(`Mayor: ${mayorNum}`);

const lista = document.getElementById("lista");
lista.innerText =`Lista: ${numArray}`

const visor = document.getElementById("visor");
visor.innerText =`Mayor: ${mayorNum}`