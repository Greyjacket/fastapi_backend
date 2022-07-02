from sqlalchemy.orm import Session
from . import models, schemas


def create_client(db: Session, client: schemas.Client):
    client = models.Client(name=client.name, phone=client.phone)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

def get_client_by_name(db: Session, name: str):
    return db.query(models.Client).filter(models.Client.name == name).first()

def get_clients(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Client).offset(skip).limit(limit).all()
 
def delete_client(db: Session, client_id: int):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    db.delete(client)
    db.commit()
    return client
