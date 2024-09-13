from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.post import Post, PostCreate
from app.crud.post import get_posts, get_post_by_id, create_post, delete_post
from app.core.database import get_db

router = APIRouter()

@router.get("/posts", response_model=List[Post])
def fetch_posts(skip: int = Query(0, ge=0),
                limit: int = Query(100, ge=1),
                db: Session = Depends(get_db)):
    """
    Fetch posts with pagination.
    
    Args:
        skip (int): The number of posts to skip. Defaults to 0.
        limit (int): The maximum number of posts to return. Defaults to 10.
        db (Session): The database session.

    Returns:
        List[Post]: A list of posts.
    """
    return get_posts(db, skip=skip, limit=limit)

@router.get("/posts/{post_id}", response_model=Post)
def fetch_post(post_id: int, db: Session = Depends(get_db)):
    """
    Fetch a specific post by its ID.

    Args:
        post_id (int): The ID of the post to retrieve.
        db (Session): The database session dependency.

    Returns:
        Post: The post with the specified ID.

    Raises:
        HTTPException: If the post with the specified ID is not found.
    """
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/posts", response_model=Post)
def add_post(post: PostCreate, db: Session = Depends(get_db)):
    """
    Create a new post and store it in the database.

    Args:
        post (PostCreate): The post data to be created.
        db (Session): The database session dependency.

    Returns:
        Post: The newly created post.
    """
    return create_post(db, post.message, post.author)

@router.delete("/posts/{post_id}", response_model=Post)
def remove_post(post_id: int, db: Session = Depends(get_db)):
    """
    Delete a post by its ID from the database.

    Args:
        post_id (int): The ID of the post to be deleted.
        db (Session): The database session dependency.

    Returns:
        Post: The deleted post.

    Raises:
        HTTPException: If the post with the specified ID is not found.
    """
    post = delete_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
