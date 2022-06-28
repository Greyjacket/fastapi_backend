from . import crud, schemas
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/properties",
)

@router.post("/", response_model=schemas.Property, tags=["Properties"])
def create_property(property: schemas.Property, db: Session = Depends(get_db)):
    property_exists = crud.get_property_by_address(db, address=property.address)
    if property_exists:
        raise HTTPException(status_code=400, detail="Property already registered")
    return crud.create_property(db=db, property=property)


@router.get("/", response_model=list[schemas.Property], tags=["Properties"])
def read_properties(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    properties = crud.get_properties(db, skip=skip, limit=limit)
    return properties


@router.get("/{address}", response_model=schemas.Property, tags=["Properties"])
def read_property(address: str, db: Session = Depends(get_db)):
    property = crud.get_property_by_address(db, address=address)
    if property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return property


@router.delete("/{property_id}", response_model=schemas.Property, tags=["Properties"])
def delete_property(property_id: int, db: Session = Depends(get_db)):
    property_exists = crud.get_property_by_id(db, id=property_id)
    if property_exists:
        property = crud.delete_property(db, property_id=property_id)
    else:
        raise HTTPException(status_code=404, detail="Property not found")
    return property
