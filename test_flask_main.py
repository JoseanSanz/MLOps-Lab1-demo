# vamos a genearar los test para evaluar la funcionalidad del endpoint flask_main.py
import io
import json
import pytest
from flask_main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Verifica que el endpoint / devuelve el mensaje correcto."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "API Flask funcionando correctamente"


def test_calculate_add(client):
    """Verifica que el endpoint /calculate realiza la suma correctamente."""
    response = client.post(
        "/calculate",
        data=json.dumps({"operation": "add", "a": 5, "b": 3}),
        content_type="application/json",
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "result" in data
    assert data["result"] == 8


def test_calculate_divide_by_zero(client):
    """Verifica que el endpoint /calculate maneja la división por cero."""
    response = client.post(
        "/calculate",
        data=json.dumps({"operation": "divide", "a": 5, "b": 0}),
        content_type="application/json",
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "División por cero no permitida"


def test_calculate_invalid_operation(client):
    """Verifica que el endpoint /calculate maneja operaciones inválidas."""
    response = client.post(
        "/calculate",
        data=json.dumps({"operation": "invalid_op", "a": 5, "b": 3}),
        content_type="application/json",
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Operación no válida"


def test_calculate_invalid_parameters(client):
    """Verifica que el endpoint /calculate maneja parámetros no numéricos."""
    response = client.post(
        "/calculate",
        data=json.dumps({"operation": "add", "a": "five", "b": 3}),
        content_type="application/json",
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Los parámetros a y b deben ser números"


def test_calculate_missing_parameters(client):
    """Verifica que el endpoint /calculate maneja parámetros faltantes."""
    response = client.post(
        "/calculate",
        data=json.dumps({"operation": "add", "a": 5}),
        content_type="application/json",
    )
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Los parámetros a y b deben ser números"
