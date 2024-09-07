import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def create_post():
    """
    Fixture to create a post and return its ID.
    """
    response = client.post("/posts", json={"message": "Hello World!", "author": "Jane Doe"})
    assert response.status_code == 200
    data = response.json()

    # Assertions to verify the post content
    assert data["message"] == "Hello World!"
    assert data["author"] == "Jane Doe"
    assert "timestamp" in data  # Check if the timestamp is present
    assert "id" in data  # Ensure the post has an id

    return data["id"]  # Return the post ID for other tests


def test_create_post(create_post):
    """
    Test to create a post using the fixture.
    """
    # This test is just to confirm that the fixture works. No assertions needed here,
    # as they are already part of the fixture.


def test_get_posts():
    """
    Test to get all posts.
    """
    response = client.get("/posts")
    assert response.status_code == 200
    data = response.json()

    # Assertions to verify the post list
    assert isinstance(data, list)  # Ensure we receive a list of posts


def test_delete_post(create_post):
    """
    Test to delete the post created by the fixture.
    """
    post_id = create_post

    # Delete the post
    response = client.delete(f"/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()

    # Assertions to verify the post was deleted correctly
    assert data["id"] == post_id
    assert data["message"] == "Hello World!"
    assert data["author"] == "Jane Doe"

    # Verify the post no longer exists
    response = client.get(f"/posts/{post_id}")
    assert response.status_code == 404  # Post should no longer exist
