from datetime import date
import json

def get_age(dob):
    today = date.today()
    birth_date = date.fromisoformat(dob)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def get_result(operation, num1, num2):
    match operation:
        case "sum":
            return { "result": num1 + num2 }, 200
        case "sub":
            return { "result": num1 - num2 }, 200
        case "mult":
            return { "result": num1 * num2 }, 200
        case "div":
            try:
                return { "result": num1 / num2 }, 200
            except ZeroDivisionError:
                return { "error": "División por cero no permitida" }, 400
        case _:
            return { "error": "Operación invalida" }, 400

def get_dni(dni: str) -> str:
    formatted_dni = ''
    for char in dni:
        try:
            if isinstance(int(char), int) and len(formatted_dni) < 8:
                formatted_dni += char
        except Exception:
            pass
    return formatted_dni

def get_balance(str_input, stack=None):
    if stack == None:
        stack = []
    
    delimiter = { '{': '}', '(': ')', '[': ']' }
    if str_input == '':
        return True if stack == [] else False
    
    if str_input[0] in list(delimiter.keys()):
        stack.append(str_input[0])
        return get_balance(str_input[1:], stack)
    else:
        if stack != [] and delimiter[stack[-1]] == str_input[0]:
            stack.pop()
            return get_balance(str_input[1:], stack)
        else:
            return False