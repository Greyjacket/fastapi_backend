from . import crud, schemas
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/clients",
)

@router.post("/", response_model=schemas.Client, tags=["Clients"])
def create_client(client: schemas.Client, db: Session = Depends(get_db)):
    client_exists = crud.get_client_by_full_name(db, full_name=client.full_name)
    if client_exists:
        raise HTTPException(status_code=400, detail="Client already registered")
    return crud.create_client(db=db, client=client)


@router.put("/{client_id}", response_model=schemas.Client,  tags=["Clients"])
def update_client(client_id: str, client: schemas.Client, db: Session = Depends(get_db)):
    client_exists = crud.get_client_by_id(db, id=client_id)
    if not client_exists:
        raise HTTPException(status_code=400, detail="Client is not registered")
    return crud.update_client(db=db, id=client_id, client=client)


@router.get("/", response_model=list[schemas.Client], tags=["Clients"])
def read_clients(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients


@router.get("/{client_name}", response_model=schemas.Client, tags=["Clients"])
def read_client(full_name: str, db: Session = Depends(get_db)):
    client = crud.get_client_by_full_name(db, full_name=full_name)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.delete("/{client_id}", response_model=schemas.Client, tags=["Clients"])
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client_exists = crud.get_client_by_id(db, id=client_id)
    if client_exists:
        client = crud.delete_client(db, client_id=client_id)
        return client
    else:
        raise HTTPException(status_code=404, detail="Client not found")
