"""
User endpoint routing
"""
# Standard library imports
from typing import List

# Third party imports
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Local application imports
from ..db.base import get_db
from ..schema.group import GroupDto, GroupCreateDto
from ..crud import group as group_crud


router = APIRouter(
    prefix='/groups',
    tags=['groups']
)


@router.get("/", response_model=List[GroupDto])
def read_groups(offset: int = 0, limit: int = 100,
                db: Session = Depends(get_db)):
    groups = group_crud.get_groups(db, offset=offset, limit=limit)
    return groups


@router.get("/{group_id}", response_model=GroupDto)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = group_crud.get_group(db, group_id=group_id)

    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")

    return db_group


@router.post("/", response_model=GroupDto)
def create_group(group: GroupCreateDto, db: Session = Depends(get_db)):
    return group_crud.create_group(db=db, group=group)