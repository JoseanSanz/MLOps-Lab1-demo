# Importamos las librerías necesarias
import io
import json
import pytest       
from fastapi_main import app    
from PIL import Image
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    """Cliente de pruebas de FastAPI."""
    return TestClient(app)

def test_home_endpoint(client):
    """Verifica que el endpoint / devuelve el mensaje correcto."""
    response = client.get("/")
    assert response.status_code == 200

def test_calculate_add(client):
    """Verifica que el endpoint /calculate realiza la suma correctamente."""
    response = client.post(
        "/calculate",
        json={"operation": "add", "a": 5, "b": 3},
    )
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert data["result"] == 8

def test_calculate_divide_by_zero(client):
    """Verifica que el endpoint /calculate maneja la división por cero."""
    response = client.post(
        "/calculate",
        json={"operation": "divide", "a": 5, "b": 0}
    )
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "División por cero no permitida"

def test_calculate_invalid_operation(client):
    """Verifica que el endpoint /calculate maneja operaciones inválidas."""
    response = client.post(
        "/calculate",
        json={"operation": "invalid_op", "a": 5, "b": 3}
    )
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Operación no válida"

def test_calculate_invalid_parameters(client):
    """Verifica que el endpoint /calculate maneja parámetros inválidos."""
    response = client.post(
        "/calculate",
        json={"operation": "add", "a": "five", "b": 3}
    )
    assert response.status_code == 422  # FastAPI devuelve 422 para errores de validación
    data = response.json()
    assert "detail" in data

def test_calculate_missing_parameters(client):
    """Verifica que el endpoint /calculate maneja parámetros faltantes."""
    response = client.post(
        "/calculate",
        json={"operation": "add", "a": 5}  # Falta 'b'
    )
    assert response.status_code == 422  # FastAPI devuelve 422 para errores de validación
    data = response.json()
    assert "detail" in data