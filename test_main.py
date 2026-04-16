from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

API_TOKEN = "my-secret-token"

def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_post_readings_unauthorized():
    data = {
        "sensor_id": "test_device",
        "temperature": 25.0,
        "humidity": 60.0,
        "light": 1,
        "obstacle": 0,
        "potentiometer": 100
    }

    response = client.post("/readings", json=data)
    assert response.status_code == 401


def test_post_readings_authorized():
    data = {
        "sensor_id": "test_device",
        "temperature": 25.0,
        "humidity": 60.0,
        "light": 1,
        "obstacle": 0,
        "potentiometer": 100
    }

    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

    response = client.post("/readings", json=data, headers=headers)
    assert response.status_code == 200


def test_get_latest():
    response = client.get("/readings/latest")
    assert response.status_code == 200


def test_get_recent():
    response = client.get("/readings/recent")
    assert response.status_code == 200
