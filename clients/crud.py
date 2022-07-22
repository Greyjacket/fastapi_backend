from sqlalchemy.orm import Session
from . import models, schemas


def create_client(db: Session, client: schemas.Client):
    client = models.Client(**client.__dict__)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

def update_client(db: Session, id: int, client: schemas.Client):
    client_to_update = db.query(models.Client).filter(models.Client.id == id).first()
    for var, value in vars(client).items():
        setattr(client_to_update, var, value) if value else None
    db.add(client_to_update)
    db.commit()
    db.refresh(client_to_update)
    return client_to_update

def get_client_by_id(db: Session, id: int):
    return db.query(models.Client).filter(models.Client.id == id).first()

def get_client_by_full_name(db: Session, full_name: str):
    return db.query(models.Client).filter(models.Client.full_name == full_name).first()

def get_clients(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Client).offset(skip).limit(limit).all()
 
def delete_client(db: Session, client_id: int):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    db.delete(client)
    db.commit()
    return client
