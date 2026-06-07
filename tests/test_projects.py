from fastapi.testclient import TestClient
from app.main import app
from app.routes.projects import PROJECTS

client = TestClient(app)


def setup_function():
    PROJECTS.clear()


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "ApiCrate"


def test_create_project():
    response = client.post(
        "/projects",
        json={"name": "Failsafe", "description": "First project"}
    )
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["name"] == "Failsafe"


def test_duplicate_project_name_rejected():
    client.post("/projects", json={"name": "Failsafe", "description": "One"})
    response = client.post("/projects", json={"name": "failsafe", "description": "Two"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Project with this name already exists"


def test_short_name_rejected():
    response = client.post("/projects", json={"name": "ab", "description": "Too short"})
    assert response.status_code == 422