const container = document.getElementById("container");

const tabla = document.createElement("table");
tabla.innerHTML = ` 
    <table id="tabla">
        <tr>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Email</th>
            <th>Nombre De la Empresa</th>
            <th>Direccion</th>
        </tr>
    </table>
`;

container.appendChild(tabla);

function insertarPersona(persona) {
    const fila = document.createElement("tr");
    let nombreApellido = persona.name.split(" ") 
    fila.innerHTML = `
        <td>${nombreApellido[0]}</td>
        <td>${nombreApellido[1]}</td>
        <td>${persona.email}</td>
        <td>${persona.company.name}</td>
        <td>${persona.address.street}, ${persona.address.suite}, ${persona.address.city} </td>
    `;

    tabla.appendChild(fila);
}

fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error en la solicitud');
        }
    })
    .then(data => {
        data.forEach(persona => {
            insertarPersona(persona)
        });
    })
    .catch(error => {
        console.error('Error al obtener los datos:', error);
});