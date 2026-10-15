from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/api/health")
    assert resp.status_code == 201
    assert resp.json() == {"status": "ok"}


def test_message():
    resp = client.get("/api/message")
    assert resp.status_code == 200
    assert "message" in resp.json()


def test_greet():
    resp = client.post("/api/greet", json={"name": "tom", "times": 2})
    assert resp.status_code == 200
    data = resp.json()
    assert data["message"].count("Hello, tom!") == 2
    assert data["from"] == "backend"


def test_greet_default():
    resp = client.post("/api/greet", json={})
    assert resp.status_code == 200
    assert resp.json()["message"] == "Hello, world!"
