const eventos = [
    {
        titulo: "Reunión de equipo",
        hora: "10:00",
        descripcion: "Reunión para discutir los próximos proyectos."
    },
    {
        titulo: "Almuerzo",
        hora: "13:00",
        descripcion: "Almuerzo con colegas en el restaurante cercano."
    },
    {
        titulo: "Clase de Yoga",
        hora: "17:30",
        descripcion: "Clase de yoga en el gimnasio local."
    }
]

const container = document.getElementById("container");

const calendar = document.createElement("table");
calendar.innerHTML = ` 
    <table id="table">
        <thead>
            <tr>
                <th>Fecha</th>
                <th>Evento</th>
                <th>Descripcion</th>
            </tr>
        </thead>
        <tbody>
            
        </tbody>
    </table>
`;

container.appendChild(calendar);
const tbody = calendar.querySelector("tbody");

function insertarEvento(evento) {
    const fila = document.createElement("tr");
    const fechaActual = new Date();
    fila.innerHTML = `
        <td>${fechaActual.toDateString()} - ${evento.hora}</td>
        <td>${evento.titulo}</td>
        <td>${evento.descripcion}</td>
    `;

    tbody.appendChild(fila);
}

eventos.forEach(evento => {
    insertarEvento(evento);
});
