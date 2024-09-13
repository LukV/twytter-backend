from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    """Schema for creating a new user"""
    first_name: Optional[str] = None  
    last_name: Optional[str] = None
    email: EmailStr  
    password: str  
    handle: str  

class User(BaseModel):
    """Schema for returning user data to the client"""
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr
    handle: str
    timestamp: datetime  # Timestamp for when the user was created

    model_config = ConfigDict(from_attributes=True)

class UserInDB(User):
    """Schema for representing a user in the database with hashed password"""
    hashed_password: str
