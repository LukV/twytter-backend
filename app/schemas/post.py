"""Pydantic models for request/response validation"""
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class Post(BaseModel):
    """Posts pydantic model"""
    message: str
    author: str
    timestamp: datetime = None
    
    model_config = ConfigDict(from_attributes=True)  # To map Pydantic to SQLAlchemy models

