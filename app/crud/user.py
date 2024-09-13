"""CRUD functions to interact with the database"""
from sqlalchemy.orm import Session
from app.models.dbmodel import UserDB
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password

def get_user_by_id(db: Session, user_id: int):
    """Fetch a user by their ID."""
    return db.query(UserDB).filter(UserDB.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """Fetch a user by their email."""
    return db.query(UserDB).filter(UserDB.email == email).first()

def get_user_by_handle(db: Session, handle: str):
    """Fetch a user by their handle."""
    return db.query(UserDB).filter(UserDB.handle == handle).first()

def create_user(db: Session, user: UserCreate):
    """Create a new user in the database."""
    hashed_password = hash_password(user.password)  # Hash the password
    db_user = UserDB(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        handle=user.handle,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    """Authenticate a user by their email and password."""
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
