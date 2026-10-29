import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.database import init_db

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_crear_usuario():
    response = client.post(
        "/usuarios/",
        json={
            "nombre": "Test User",
            "email": "test@test.mx",
            "telefono": "5551234567",
            "es_trabajador": False,
            "es_cliente": True
        }
    )
    assert response.status_code == 201
    assert response.json()["nombre"] == "Test User"

def test_listar_trabajadores():
    response = client.get("/trabajadores/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
