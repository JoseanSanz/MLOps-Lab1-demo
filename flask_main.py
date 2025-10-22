#!/usr/bin/env python

# Generar una aplicacion Flask para utilizar las funciones de calculadora del modulo mylib.calculator
from flask import Flask, request, jsonify
from mylib.calculator import add, subtract, multiply, divide, power

# from pathlib import Path
# import json

# Configuración de Flask
app = Flask(__name__)


# Crea un endpoint rest que devuelva un mensaje de estado
@app.route("/")
def home():
    return "API Flask funcionando correctamente"


# Crea un endpoint rest que realice operaciones de calculadora
@app.route("/calculate", methods=["POST"])
def calculate():
    """
    Endpoint REST para realizar operaciones de calculadora.

    Espera un JSON con:
    - operation: operación a realizar (add, subtract, multiply, divide, power)
    - a: primer número (float)
    - b: segundo número (float)
    """
    data = request.get_json()
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if operation not in ["add", "subtract", "multiply", "divide", "power"]:
        return jsonify({"error": "Operación no válida"}), 400

    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        return jsonify({"error": "Los parámetros a y b deben ser números"}), 400

    result = None
    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        if b == 0:
            return jsonify({"error": "División por cero no permitida"}), 400
        result = divide(a, b)
    elif operation == "power":
        result = power(a, b)

    return jsonify({"result": result})


# crea una ruta para docs
@app.route("/docs")
def docs():
    """Devuelve una página HTML simple con la documentación de la API."""
    html_content = """
    <html>
        <head>
            <title>Documentación de la API Flask</title>
        </head>
        <body>
            <h1>Documentación de la API Flask</h1>
            <h2>Endpoints disponibles:</h2>
            <ul>
                <li><strong>GET /</strong>: Mensaje de estado.</li>
                <li><strong>POST /calculate</strong>: Realiza operaciones de calculadora. Espera un JSON con 'operation', 'a' y 'b'.</li>
            </ul>
            <h2>Operaciones soportadas:</h2>
            <ul>
                <li>add: Suma a + b</li>
                <li>subtract: Resta a - b</li>
                <li>multiply: Multiplica a * b</li>
                <li>divide: Divide a / b (b no puede ser 0)</li>
                <li>power: Potencia a ** b</li>
            </ul>
        </body>
    </html>
    """
    return html_content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
