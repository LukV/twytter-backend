"""CRUD functions to interact with the database"""
from sqlalchemy.orm import Session
from app.models.dbmodel import HashtagDB

def get_hashtags(db: Session, skip: int = 0, limit: int = 10):
    """Fetch tags from the database with pagination."""
    return db.query(HashtagDB).offset(skip).limit(limit).all()

def get_hashtag_by_name(db: Session, hashtag: str):
    """Find a hashtag by its ID."""
    return db.query(HashtagDB).filter(HashtagDB.hashtag == hashtag).first()

def create_tag(db: Session, hashtag: str, count: int, author: str):
    """Create a new hashtag"""
    db_hashtag = HashtagDB(hashtag=hashtag, count=count, author=author)
    db.add(db_hashtag)
    db.commit()
    db.refresh(db_hashtag)
    return db_hashtag

def delete_tag(db: Session, hashtag_id: int):
    """Delete a hashtag"""
    hashtag = db.query(HashtagDB).filter(HashtagDB.id == hashtag_id).first()
    if hashtag:
        db.delete(hashtag)
        db.commit()
    return hashtag

def update_tag_count(db: Session, hashtag_id: int, increment: int = 1):
    """Increment the count of a specific hashtag."""
    hashtag = db.query(HashtagDB).filter(HashtagDB.id == hashtag_id).first()
    if hashtag:
        hashtag.count += increment
        db.commit()
        db.refresh(hashtag)
    return hashtag
