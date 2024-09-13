"""SQLAlchemy database models"""
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class PostDB(Base):
    """posts table"""
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    author = Column(String, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class HashtagDB(Base):
    """hashtags table"""
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True, index=True)
    hashtag = Column(String, index=True)
    count = Column(Integer)
    author = Column(String, index=True)
    lastupdated = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class UserDB(Base):
    """users table"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=True)  # Optional field
    last_name = Column(String, index=True, nullable=True)   # Optional field
    email = Column(String, unique=True, index=True, nullable=False)
    handle = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
