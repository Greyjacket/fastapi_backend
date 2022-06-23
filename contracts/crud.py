from sqlalchemy.orm import Session
from . import models


def get_contract(db: Session, contract_id: int):
    return db.query(models.Contract).filter(models.Contract.id == contract_id).first()


def get_contracts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contract).offset(skip).limit(limit).all()


def delete_contract(db: Session, contract_id: int):
    contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()
    db.delete(contract)
    db.commit()
    return contract
