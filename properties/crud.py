from sqlalchemy.orm import Session
import models, schemas


def create_property(db: Session, property: schemas.Property):
    property = models.Property(address=property.address, mortgage_applicaton_date=property.mortgage_applicaton_date)
    db.add(property)
    db.commit()
    db.refresh(property)
    return property

def get_property_by_address(db: Session, address: str):
    return db.query(models.Property).filter(models.Property.address == address).first()

def get_properties(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Property).offset(skip).limit(limit).all()

def delete_property(db: Session, property_id: int):
    property = db.query(models.Property).filter(models.Property.id == property_id).first()
    db.delete(property)
    db.commit()
    return property
