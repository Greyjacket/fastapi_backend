from . import crud, schemas
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/attorneys",
)

@router.post("/", response_model=schemas.Attorney)
def create_attorney(attorney: schemas.Attorney, db: Session = Depends(get_db)):
    attorney_exists = crud.get_attorney_by_name(db, name=attorney.name)
    if attorney_exists:
        raise HTTPException(status_code=400, detail="Attorney already registered")
    return crud.create_attorney(db=db, attorney=attorney)


@router.get("/", response_model=list[schemas.Attorney])
def read_attorneys(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    attorneys = crud.get_attorneys(db, skip=skip, limit=limit)
    return attorneys


@router.get("/{attorney_name}", response_model=schemas.Attorney)
def read_attorney(name: str, db: Session = Depends(get_db)):
    attorney = crud.get_attorney_by_name(db, name=name)
    if attorney is None:
        raise HTTPException(status_code=404, detail="Attorney not found")
    return attorney


@router.delete("/{attorney_id}", response_model=schemas.Attorney)
def delete_attorney(attorney_id: int, db: Session = Depends(get_db)):
    attorney = crud.delete_attorney(db, attorney_id=attorney_id)
    if attorney is None:
        raise HTTPException(status_code=404, detail="Attorney not found")
    return attorney
