from sqlalchemy.orm import Session
from . import models, schemas


def create_album(db: Session, album: schemas.Album):
    album = models.Album(**album.__dict__)
    db.add(album)
    db.commit()
    db.refresh(album)
    return album

def update_album(db: Session, id: int, album: schemas.Album):
    album_to_update = db.query(models.Album).filter(models.Album.id == id).first()
    for var, value in vars(album).items():
        setattr(album_to_update, var, value) if value else None
    db.add(album_to_update)
    db.commit()
    db.refresh(album_to_update)
    return album_to_update

def get_album_by_id(db: Session, id: int):
    return db.query(models.Album).filter(models.Album.id == id).first()

def get_album_by_full_name(db: Session, full_name: str):
    return db.query(models.Album).filter(models.Album.full_name == full_name).first()

def get_albums(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Album).offset(skip).limit(limit).all()
 
def delete_album(db: Session, album_id: int):
    album = db.query(models.Album).filter(models.Album.id == album_id).first()
    db.delete(album)
    db.commit()
    return album
