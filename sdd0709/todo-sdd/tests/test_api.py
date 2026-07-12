import os
import pytest
from fastapi.testclient import TestClient

from app.database import Base, engine
from app.main import app


@pytest.fixture(autouse=True)
def reset_db():
    os.environ["DATABASE_URL"] = "sqlite:///./test_todos.db"
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_todo_and_list(client):
    response = client.post("/api/todos", json={"title": "테스트 할 일"})
    assert response.status_code == 200

    response = client.get("/api/todos")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "테스트 할 일"
    assert data[0]["completed"] is False


def test_create_todo_rejects_blank_title(client):
    response = client.post("/api/todos", json={"title": "   "})
    assert response.status_code == 422


def test_toggle_and_delete_todo(client):
    create_response = client.post("/api/todos", json={"title": "토글 테스트"})
    todo_id = create_response.json()["id"]

    toggle_response = client.patch(f"/api/todos/{todo_id}", json={"completed": True})
    assert toggle_response.status_code == 200
    assert toggle_response.json()["completed"] is True

    delete_response = client.delete(f"/api/todos/{todo_id}")
    assert delete_response.status_code == 200
    assert client.get(f"/api/todos/{todo_id}").status_code == 404


def test_filter_and_count(client):
    client.post("/api/todos", json={"title": "완료 전"})
    todo = client.post("/api/todos", json={"title": "완료 후"}).json()
    client.patch(f"/api/todos/{todo['id']}", json={"completed": True})

    all_response = client.get("/api/todos")
    active_response = client.get("/api/todos?status=active")
    completed_response = client.get("/api/todos?status=completed")

    assert len(all_response.json()) == 2
    assert len(active_response.json()) == 1
    assert len(completed_response.json()) == 1
    assert active_response.json()[0]["title"] == "완료 전"
    assert completed_response.json()[0]["title"] == "완료 후"


def test_root_page_renders_ui(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "todo-app" in response.text.lower()
