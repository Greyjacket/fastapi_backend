from sqlalchemy.orm import Session
from . import models, schemas


def create_attorney(db: Session, attorney: schemas.Attorney):
    attorney = models.Attorney(name=attorney.name, phone=attorney.phone)
    db.add(attorney)
    db.commit()
    db.refresh(attorney)
    return attorney

def get_attorney_by_name(db: Session, name: str):
    return db.query(models.Attorney).filter(models.Attorney.name == name).first()

def get_attorney_by_id(db: Session, attorney_id: int):
    return db.query(models.Attorney).filter(models.Attorney.id == attorney_id).first()

def get_attorneys(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Attorney).offset(skip).limit(limit).all()

def delete_attorney(db: Session, attorney_id: int):
    attorney = db.query(models.Attorney).filter(models.Attorney.id == attorney_id).first()
    db.delete(attorney)
    db.commit()
    return attorney

    # property_exists = crud.get_property_by_id(db, id=property_id)
    # if property_exists:
    #     property = crud.delete_property(db, property_id=property_id)
    # else:
    #     raise HTTPException(status_code=404, detail="Property not found")
    # return property