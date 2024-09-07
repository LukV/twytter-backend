"""Route for post-related operations"""
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.post import Post
from app.crud.post import get_posts, create_post
from app.core.database import get_db

router = APIRouter()

@router.get("/posts", response_model=List[Post])
def fetch_posts(db: Session = Depends(get_db)):
    return get_posts(db)

@router.post("/posts", response_model=Post)
def add_post(post: Post, db: Session = Depends(get_db)):
    return create_post(db, post.message, post.author)
