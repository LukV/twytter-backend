"""SQLAlchemy database models"""
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class PostDB(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    author = Column(String, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
