from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class TagUpdate(BaseModel):
    """Schema for incrementing the count for a tag"""
    increment_by: int = 1

class TagCreate(BaseModel):
    """Schema for creating a tag"""
    hashtag: str
    author: str
    count: int = Field(default=1, exclude=True)  

class Tag(BaseModel):
    """Schema for returning tag data to the client"""
    id: int
    hashtag: str
    count: int
    author: str
    lastupdated: datetime
    
    model_config = ConfigDict(from_attributes=True)  # To map Pydantic to SQLAlchemy models
