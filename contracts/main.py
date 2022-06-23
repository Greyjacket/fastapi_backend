from . import crud, schemas
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/contracts",
)

@router.post("/", response_model=schemas.Contract)
def create_contract(contract: schemas.Contract, db: Session = Depends(get_db)):
    return crud.create_contract(db=db, contract=contract)


@router.get("/", response_model=list[schemas.Contract])
def read_contracts(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    contracts = crud.get_contracts(db, skip=skip, limit=limit)
    return contracts


@router.get("/{contract_id}", response_model=schemas.Contract)
def read_contract(contract_id: int, db: Session = Depends(get_db)):
    property = crud.get_property_by_address(db, address=contract_id)
    if property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return property


@router.delete("/{property_id}", response_model=schemas.Contract)
def delete_property(property_id: int, db: Session = Depends(get_db)):
    property_exists = crud.get_property_by_id(db, id=property_id)
    if property_exists:
        property = crud.delete_property(db, property_id=property_id)
    else:
        raise HTTPException(status_code=404, detail="Property not found")
    return property
