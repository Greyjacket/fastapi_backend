from sqlalchemy.orm import Session
from . import models, schemas


def create_property(db: Session, attorney: schemas.Attorney):
    attorney = models.Attorney(name=attorney.name, phone=attorney.phone)
    db.add(attorney)
    db.commit()
    db.refresh(attorney)
    return attorney

def get_attorney_by_name(db: Session, name: str):
    return db.query(models.Attorney).filter(models.Attorney.name == name).first()

def get_attornies(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Attorney).offset(skip).limit(limit).all()

def delete_attorney(db: Session, attorney_id: int):
    attorney = db.query(models.Property).filter(models.Attorney.id == attorney_id).first()
    db.delete(attorney)
    db.commit()
    return attorney
