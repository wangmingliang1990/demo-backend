from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/api/health")
    assert resp.status_code == 200
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
    # 同步更新：消息尾部新增了 " [auto-deployed by CI]" 后缀，
    # 这是全仓库唯一一条"精确相等"断言，所以只有这一条测试需要跟着改
    assert resp.json()["message"] == "Hello, world! [auto-deployed by CI]"
