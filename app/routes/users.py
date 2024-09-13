from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
from app.crud.user import get_user_by_id, get_user_by_email, create_user
from app.core.database import get_db

router = APIRouter()

@router.post("/users", response_model=User)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user and store it in the database.

    Args:
        user (UserCreate): The user data to be created.
        db (Session): The database session dependency.

    Returns:
        User: The newly created user.

    Raises:
        HTTPException: If the email is already registered.
    """
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db, user)

@router.get("/users/{user_id}", response_model=User)
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    """
    Fetch a specific user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.
        db (Session): The database session dependency.

    Returns:
        User: The user with the specified ID.

    Raises:
        HTTPException: If the user with the specified ID is not found.
    """
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
