from ..models.film_model import Film
from ..models.exceptions import FilmNotFound, InvalidDataError

from flask import request

from decimal import Decimal

class FilmController:
    """Film controller class"""

    @classmethod
    def get(cls, film_id):
        """Get a film by id"""
        film = Film(film_id=film_id)
        result = Film.get(film)

        if result is None:
            raise FilmNotFound(film_id)

        return result.serialize(), 200
        
    @classmethod
    def get_all(cls):
        """Get all films"""
        film_objects = Film.get_all()
        films = []
        for film in film_objects:
            films.append(film.serialize())
        return films, 200
    
    @classmethod
    def create(cls):
        """Create a new film"""
        data = request.json
        
        validated_data = cls.validate_data(data)

        film = Film(**validated_data)
        Film.create(film)
        return {'message': 'Film created successfully'}, 201

    @classmethod
    def update(cls, film_id):
        """Update a film"""
        data = request.json

        if not Film.exists(film_id):
            raise FilmNotFound(film_id)

        validated_data = cls.validate_data(data)

        validated_data['film_id'] = film_id

        film = Film(**validated_data)

        Film.update(film)
        return {'message': 'Film updated successfully'}, 200
    
    @classmethod
    def delete(cls, film_id):
        """Delete a film"""
        if not Film.exists(film_id):
            raise FilmNotFound(film_id)

        film = Film(film_id=film_id)
        Film.delete(film)

        return {'message': 'Film deleted successfully'}, 204
    
    @classmethod
    def validate_data(cls, data):
        """Validate film data"""
        if len(data.get('title', '')) < 3:
            raise InvalidDataError("Title must have at least three characters")

        language_id = data.get('language_id')
        if not isinstance(language_id, int):
            raise InvalidDataError("Language ID must be an integer")

        rental_duration = data.get('rental_duration')
        if not isinstance(rental_duration, int):
            raise InvalidDataError("Rental duration must be an integer")

        rental_rate = data.get('rental_rate')
        if rental_rate is not None:
            if not isinstance(rental_rate, int):
                raise InvalidDataError("Rental rate must be an integer")
            data['rental_rate'] = Decimal(rental_rate) / 100

        replacement_cost = data.get('replacement_cost')
        if replacement_cost is not None:
            if not isinstance(replacement_cost, int):
                raise InvalidDataError("Replacement cost must be an integer")
            data['replacement_cost'] = Decimal(replacement_cost) / 100

        special_features = data.get('special_features')
        if not isinstance(special_features, list):
            raise InvalidDataError("Special features must be a list")

        valid_special_features = ["Trailers", "Commentaries", "Deleted Scenes", "Behind the Scenes"]
        for feature in special_features:
            if feature not in valid_special_features:
                raise InvalidDataError(f"Invalid special feature: {feature}")

        return data