from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.tag import Tag, TagCreate, TagUpdate
from app.crud.tag import get_tags, get_hashtag_by_id, create_tag, delete_tag, update_tag_count
from app.core.database import get_db

router = APIRouter()

@router.get("/tags", response_model=List[Tag])
def fetch_tags(skip: int = Query(0, ge=0), 
               limit: int = Query(10, ge=1), 
               db: Session = Depends(get_db)):
    """
    Fetch tags with pagination.

    Args:
        skip (int): The number of tags to skip. Defaults to 0.
        limit (int): The maximum number of tags to return. Defaults to 10.
        db (Session): The database session.

    Returns:
        List[Tag]: A list of tags.
    """
    return get_tags(db, skip=skip, limit=limit)

@router.get("/tags/{hashtag_id}", response_model=Tag)
def fetch_tag(hashtag_id: int, db: Session = Depends(get_db)):
    """
    Fetch a specific tag by its ID.

    Args:
        hashtag_id (int): The ID of the tag to retrieve.
        db (Session): The database session.

    Returns:
        Tag: The tag with the specified ID.

    Raises:
        HTTPException: If the tag with the specified ID is not found.
    """
    tag = get_hashtag_by_id(db, hashtag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@router.post("/tags", response_model=Tag)
def add_tag(tag: TagCreate, db: Session = Depends(get_db)):
    """
    Create a new tag and store it in the database.

    Args:
        tag (TagCreate): The tag data to be created.
        db (Session): The database session dependency.

    Returns:
        Tag: The newly created tag.
    """
    return create_tag(db, tag.hashtag, tag.count, tag.author)

@router.delete("/tags/{hashtag_id}", response_model=Tag)
def remove_tag(hashtag_id: int, db: Session = Depends(get_db)):
    """
    Delete a tag by its ID from the database.

    Args:
        hashtag_id (int): The ID of the tag to be deleted.
        db (Session): The database session dependency.

    Returns:
        Tag: The deleted tag.

    Raises:
        HTTPException: If the tag with the specified ID is not found.
    """
    tag = delete_tag(db, hashtag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@router.put("/tags/{hashtag_id}", response_model=Tag)
def update_tag_count_route(hashtag_id: int, tag_update: TagUpdate, db: Session = Depends(get_db)):
    """
    Update the count of a specific tag (e.g. increment the count).

    Args:
        hashtag_id (int): The ID of the tag to update.
        tag_update (TagUpdate): The data to update (e.g. the increment count).
        db (Session): The database session dependency.

    Returns:
        Tag: The updated tag.

    Raises:
        HTTPException: If the tag with the specified ID is not found.
    """
    tag = update_tag_count(db, hashtag_id, increment=tag_update.increment)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag
