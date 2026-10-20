import pytest
from app import app, tasks


@pytest.fixture
def client():
    app.config["TESTING"] = True
    tasks.clear()
    with app.test_client() as c:
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_home_page(client):
    assert client.get("/").status_code == 200


def test_add_and_list_task(client):
    r = client.post("/api/tasks", json={"title": "Write report"})
    assert r.status_code == 201
    assert client.get("/api/tasks").get_json()[0]["title"] == "Write report"


def test_add_task_requires_title(client):
    assert client.post("/api/tasks", json={"title": "  "}).status_code == 400


def test_toggle_task(client):
    client.post("/api/tasks", json={"title": "x"})
    assert client.put("/api/tasks/1").get_json()["done"] is True


def test_delete_task(client):
    client.post("/api/tasks", json={"title": "x"})
    assert client.delete("/api/tasks/1").status_code == 204
    assert client.get("/api/tasks").get_json() == []


def test_missing_task(client):
    assert client.put("/api/tasks/99").status_code == 404
    assert client.delete("/api/tasks/99").status_code == 404
