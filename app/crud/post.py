"""CRUD functions to interact with the database"""
from sqlalchemy.orm import Session
from app.models.post import PostDB

def get_posts(db: Session):
    return db.query(PostDB).all()

def create_post(db: Session, message: str, author: str):
    db_post = PostDB(message=message, author=author)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
