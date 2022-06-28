from . import crud, schemas
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/contracts",
)

@router.post("/", response_model=schemas.Contract, tags=["Contracts"])
def create_contract(contract: schemas.Contract, db: Session = Depends(get_db)):
    return crud.create_contract(db=db, contract=contract)


@router.get("/", response_model=list[schemas.Contract], tags=["Contracts"])
def read_contracts(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    contracts = crud.get_contracts(db, skip=skip, limit=limit)
    return contracts


@router.get("/{contract_id}", response_model=schemas.Contract, tags=["Contracts"])
def read_contract(contract_id: int, db: Session = Depends(get_db)):
    property = crud.get_contract(db, contract_id=contract_id)
    if property is None:
        raise HTTPException(status_code=404, detail="Contract not found")
    return property


@router.delete("/{contract_id}", response_model=schemas.Contract, tags=["Contracts"])
def delete_contract(contract_id: int, db: Session = Depends(get_db)):
    contract_exists = crud.get_contract_by_id(db, id=contract_id)
    if contract_exists:
        contract = crud.delete_contract(db, contract_id=contract_id)
    else:
        raise HTTPException(status_code=404, detail="Contract not found")
    return contract
