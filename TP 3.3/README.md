# TP 3.3

El objeto de este trabajo es poner en práctica los conocimientos adquiridos en el módulo sobre manejo de errores y excepciones, y serialización de objetos.
Para ello se brindará una API con algunas rutas implementadas, y se solicitará implementar manejadores de errores para las mismas, además de realizar algunas modificaciones en el código para mejorar su legibilidad y mantenibilidad. Se empleará la base de datos sakila de MySQL, particularmente la tabla film para obtener información de películas.

Por último, en clase se estableció que existen varias alternativas para definir excepciones personalizadas, como heredar de HTTPException de werkzeug.exceptions. En este trabajo se solicita definir excepciones personalizadas heradando de la siguiente clase: 

```python
class CustomException(Exception): 
    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__() 
        self.description = description 
        self.name = name 
        self.status_code = status_code
```

Al realizar una petición GET a la ruta /films/<int:film_id> se obtiene información de una película por su ID. Sin embargo, si el ID no existe, se producirá un error debido a que el controlador no está preparado para manejar esta situación. Es decir, no devolvemos una respuesta con un formato adecuado para el cliente.
Por lo tanto, se solicita implementar una excepción personalizada llamada FilmNotFound que herede de la clase CustomException y que se lance cuando no se encuentre una película por su ID.
Por supuesto, se debe definir un manejador para esta excepción, y registrar el manejador en la aplicación.
Una vez completado lo anterior, este deberá devolver una respuesta con formato JSON y un código de estado HTTP 404. El cuerpo de la respuesta debe tener el siguiente formato:

{ "error": { "code": 404, "name": "Film Not Found", "description": "Film with id {film_id} not found" } }


Ejercicio 2

Al registrar una nueva película con un método POST para el endpoint /films/ algunos datos son obligatorios, como el id de la película, título, id del idioma, duración del alquiler, precio del alquiler, costo de reemplazo y última actualización.
Los datos son ingresados por el usuario, por lo tanto, se solicita validar los datos de entrada:
• El atributo title debe tener tres caracteres como mínimo.
• Los atributos language_id y rental_duration deben ser números enteros.
• Como hemos mencionado, los atributos rental_rate y replacement_cost son de tipo Decimal en la base de datos y los convertimos a un número entero multiplicando por 100 al momento de serializar la película. No obstante, no existe una validación para estos campos al momento de registrar una nueva película. Por lo tanto, se solicita validar que estos campos sean números enteros.
• En cuanto al atributo last_update y el id de la película, estos son generados automáticamente por la base de datos y en la misma consulta de inserción. Por lo tanto, no deben ser ingresados por el usuario, pues serán ignorados.
Por último, para el atributo special_features se solicita validar que el valor ingresado sea una lista de strings, y que cada string sea uno de los siguientes: Trailers, Commentaries, Deleted Scenes, Behind the Scenes.

Ayuda: para validar que un valor sea una lista de strings, se puede emplear la función isinstance de Python. Por ejemplo, isinstance(data.get('special_features'), list) devuelve True si el valor de special_features es una lista, o False en caso contrario.

Recordemos que debemos validar también que cada string sea uno de los mencionados anteriormente.

Si no se cumplen las validaciones mencionadas, se debe lanzar una excepción personalizada llamada InvalidDataError con un código de estado HTTP 400, la cual hereda de la clase CustomException. Por supuesto, se debe definir un manejador para esta excepción, y registrar el manejador en la aplicación.