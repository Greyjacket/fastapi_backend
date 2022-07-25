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

def get_album_by_title(db: Session, title: str):
    return db.query(models.Album).filter(models.Album.title == title).first()

def get_albums(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Album).offset(skip).limit(limit).all()
 
def delete_album(db: Session, album_id: int):
    album = db.query(models.Album).filter(models.Album.id == album_id).first()
    db.delete(album)
    db.commit()
    return album

def create_artist(db: Session, artist: schemas.Artist):

    artist = models.Artist(**artist.__dict__)
    db.add(artist)
    db.commit()
    db.refresh(artist)
    return artist

def update_artist(db: Session, id: int, artist: schemas.Artist):
    artist_to_update = db.query(models.Artist).filter(models.Artist.id == id).first()
    for var, value in vars(artist).items():
        setattr(artist_to_update, var, value) if value else None
    db.add(artist_to_update)
    db.commit()
    db.refresh(artist_to_update)
    return artist_to_update

def get_artist_by_id(db: Session, id: int):
    return db.query(models.Artist).filter(models.Artist.id == id).first()

def get_artist_by_full_name(db: Session, name: str):
    return db.query(models.Artist).filter(models.Artist.name == name).first()

def get_artists(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Artist).offset(skip).limit(limit).all()
 
def delete_artist(db: Session, artist_id: int):
    artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    db.delete(artist)
    db.commit()
    return artist


def create_track(db: Session, track: schemas.Track):
    track = models.Track(**track.__dict__)
    db.add(track)
    db.commit()
    db.refresh(track)
    return track

def update_track(db: Session, id: int, track: schemas.Track):
    track_to_update = db.query(models.Track).filter(models.Track.id == id).first()
    for var, value in vars(track).items():
        setattr(track_to_update, var, value) if value else None
    db.add(track_to_update)
    db.commit()
    db.refresh(track_to_update)
    return track_to_update

def get_track_by_id(db: Session, id: int):
    return db.query(models.Track).filter(models.Track.id == id).first()

def get_track_by_title(db: Session, title: str):
    return db.query(models.Track).filter(models.Track.title == title).first()

def get_tracks(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Track).offset(skip).limit(limit).all()
 
def delete_track(db: Session, track_id: int):
    track = db.query(models.Track).filter(models.Track.id == track_id).first()
    db.delete(track)
    db.commit()
    return track