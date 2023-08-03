// Crear un objeto persona que contenga nombre, apellido, edad, sexo y teléfono. Luego crear una tabla (con JavaScript) e insertar los datos con su respectivo encabezado.

const persona0 = {
    nombre: "John",
    apellido: "Doe", 
    edad: 25,
    sexo: 'Masculino',
    telefono: 387446623
}

const persona1 = {
    nombre: "María",
    apellido: "González",
    edad: 30,
    sexo: 'Femenino',
    telefono: 555123456
};

const persona2 = {
    nombre: "Carlos",
    apellido: "Ramírez",
    edad: 40,
    sexo: 'Masculino',
    telefono: 654987321
};

let personas = [persona0, persona1, persona2]

const container = document.getElementById("container");

const tabla = document.createElement("table");
tabla.innerHTML = ` 
    <table id="tablaPersonas">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Apellido</th>
                <th>Edad</th>
                <th>Sexo</th>
                <th>Teléfono</th>
            </tr>
        </thead>
        <tbody>
            
        </tbody>
    </table>
`;

container.appendChild(tabla);
const tbody = tabla.querySelector("tbody");

function insertarPersona(persona) {
    const fila = document.createElement("tr");
    fila.innerHTML = `
        <td>${persona.nombre}</td>
        <td>${persona.apellido}</td>
        <td>${persona.edad}</td>
        <td>${persona.sexo}</td>
        <td>${persona.telefono}</td>
    `;

    tbody.appendChild(fila);
}

personas.forEach(persona => {
    insertarPersona(persona);
});
