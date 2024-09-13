"""CRUD functions to interact with the database"""
from sqlalchemy.orm import Session
from app.models.dbmodel import PostDB

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    """Fetch posts from the database with pagination."""
    return db.query(PostDB).offset(skip).limit(limit).all()

def get_post_by_id(db: Session, post_id: int):
    return db.query(PostDB).filter(PostDB.id == post_id).first()

def create_post(db: Session, message: str, author: str):
    db_post = PostDB(message=message, author=author)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    post = db.query(PostDB).filter(PostDB.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post
