from flask import Flask, jsonify, request
from config import Config
from datetime import date
import json
from .endpoints import get_age, get_result, get_dni, get_balance

def init_app():
    """Crea y configura la aplicacion Flask"""
    
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER)
    
    app.config.from_object(Config)
    
    @app.route("/")
    def welcome():
        response = { "message": "Bienvenidx!" }
        return jsonify(response), 200
    
    @app.route("/info")
    def info():
        app_name = app.config.get("APP_NAME", "Default")
        response = { "message": f"Bienvenidx a {app_name}" }
        return jsonify(response), 200
    
    @app.route("/about")
    def about():
        response = {
            "app_name": app.config.get("APP_NAME"),
            "description": app.config.get("APP_DESC"),
            "developers": app.config.get("APP_DEVS"),
            "version": app.config.get("APP_VER")
        }
        return jsonify(response), 200
    
    @app.route("/sum/<int:num1>/<int:num2>")
    def addition(num1, num2):
        try:
            return jsonify( { "total": num1 + num2 } ), 200
        except Exception as e:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
    
    @app.route("/age/<dob>")
    def age(dob):
        try:
            age = get_age(dob)
            if age < 0:
                response = {'error': 'Fecha de nacimiento futura'}
                return jsonify(response), 400
            return jsonify( {'age': age} ), 200
        except Exception as e:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
                                    
    @app.route("/operate")
    def operate():
        try:
            operation = request.args.get("operation")
            num1 = int(request.args.get("num1"))
            num2 = int(request.args.get("num2"))
            result = get_result(operation, num1, num2)
            return jsonify(result[0]), result[1]
        except Exception as e:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
    
    @app.route("/title/<string:word>")
    def format_word(word: str):
        try:
            return jsonify( { "formatted_word": word.capitalize() }), 200
        except Exception as e:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
    
    @app.route("/formatted/<string:dni>")
    def format_dni(dni: str):
        try:
            formatted_dni = get_dni(dni)
            if formatted_dni[:2] == "00" or len(formatted_dni) < 8:
                raise Exception
            else:
                return jsonify( { "formatted_dni": formatted_dni }), 200 
        except Exception as e:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
    
    @app.route("/format")
    def format_user():
        try:
            firstname = request.args.get("firstname")
            lastname = request.args.get("lastname")
            dob = request.args.get("dob")
            dni = request.args.get("dni")

            age_format = get_age(dob)
            formatted_dni = get_dni(dni)

            if age_format < 0:
                return jsonify({'error': 'Fecha de nacimiento futura'}), 400
            if formatted_dni[:2] == "00" or len(formatted_dni) < 8:
                return jsonify({'error': 'DNI invalido'}), 400

            response = {
                "firstname": firstname.capitalize(),
                "lastname": lastname.capitalize(),
                "age": age_format,
                "dni": formatted_dni
            }

            return jsonify( response ), 200
        except Exception as e:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
    
    @app.route("/encode/<string:keyword>")
    def morse_encoder(keyword: str):
        try:
            json_path = app.config['STATIC_FOLDER'] + 'morse_code.json'
            encode_msg = ""
            with open(json_path, "r") as file:
                morse_data = json.load(file)["letters"]
            for letter in keyword:
                if letter == "+":
                    encode_msg += "^+"
                else:
                    encode_msg += f"{morse_data[letter.upper()]}+"
            if len(encode_msg[:-1]) <= 100:
                return jsonify( {'morse': encode_msg[:-1]} ), 200
            else:
                return jsonify( {'error': 'La palabra clave sobrepasa los 100 caracteres'} ), 400
        except Exception:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
    
    @app.route("/decode/<string:morse_code>")
    def morse_decoder(morse_code: str):
        try:
            json_path = app.config['STATIC_FOLDER'] + 'morse_code.json'
            encoded = morse_code.split("+") 
            decoded = ""
            with open(json_path, "r") as file:
                morse_data = json.load(file)["letters"]
            for letter in encoded:
                for key, val in morse_data.items():
                    if val == letter:
                        decoded += key
            return jsonify({ "decodificado": decoded.capitalize() }), 200
        except Exception:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
    
    @app.route("/convert/binary/<string:num>")
    def convert_binary(num):
        try:
            decimal = 0
            for i in range(len(num)):
                digit = int(num[i])
                pos = len(num) - i - 1
                decimal += digit * (2 ** pos)
            return jsonify( { "decimal": decimal } ), 200
        except Exception:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
    
    @app.route("/balance/<string:input>")
    def balance(input):
        try:
            response = get_balance(input) 
            return jsonify( { "balance": response } ), 200
        except Exception:
            return jsonify( {'error': 'Ha ocurrido un error'} ), 400
            
        

    return app