"""
Item endpoint routing
"""
# Standard library imports
from typing import List

# Third party imports
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Local application imports
from ..db.base import get_db
from ..schema.item import Item
from ..crud.item import get_items


router = APIRouter(
    prefix='/items',
    tags=['items']
)


@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items