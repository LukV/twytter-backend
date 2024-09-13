"""Post pydantic schema"""
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class PostCreate(BaseModel):
    """Schema for creating a post"""
    message: str

class Post(BaseModel):
    """Schema for returning post data to the client"""
    id: int
    message: str
    author: str
    timestamp: datetime
    
    model_config = ConfigDict(from_attributes=True)  # To map Pydantic to SQLAlchemy models
