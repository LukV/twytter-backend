from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_post():
    response = client.post("/posts", json={"message": "Hello World!", "author": "Jane Doe"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello World!"
    assert data["author"] == "Jane Doe"
    assert "timestamp" in data  # Check if the timestamp is present

def test_get_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Ensure we receive a list of posts
