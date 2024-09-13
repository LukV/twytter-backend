import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import Base, get_db

# Setup the test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override to use test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Apply the database override for testing
app.dependency_overrides[get_db] = override_get_db

# Create the test client
client = TestClient(app)

# Create tables in the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_register_user():
    response = client.post("/users", json={
        "first_name": "Test",
        "last_name": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "handle": "@TestUser"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

def test_login_user():
    response = client.post("/login", data={
        "username": "testuser@example.com",  # Using email as username
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    return response.json()["access_token"]

def test_add_post():
    token = test_login_user()  # Get the JWT token
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/posts", json={"message": "Hello world!"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Hello world!"

def test_get_post():
    response = client.get("/posts/1")  # Assuming the post created has ID 1
    assert response.status_code == 200
    assert response.json()["message"] == "Hello world!"

def test_delete_post():
    token = test_login_user()  # Get the JWT token
    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/posts/1", headers=headers)  # Assuming the post has ID 1
    assert response.status_code == 200

def test_delete_user():
    # This assumes the user can be deleted, but depending on your system's rules, you might
    # not allow users to delete their own account.
    pass
