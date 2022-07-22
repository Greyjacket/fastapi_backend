from . import crud, schemas
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/music",
)

@router.post("/albums", response_model=schemas.Album, tags=["Albums"])
def create_album(album: schemas.Album, db: Session = Depends(get_db)):
    album_exists = crud.get_album_by_full_name(db, full_name=album.full_name)
    if album_exists:
        raise HTTPException(status_code=400, detail="Album already registered")
    return crud.create_album(db=db, album=album)


@router.put("/{album_id}", response_model=schemas.Album,  tags=["Albums"])
def update_album(album_id: str, album: schemas.Album, db: Session = Depends(get_db)):
    album_exists = crud.get_album_by_id(db, id=album_id)
    if not album_exists:
        raise HTTPException(status_code=400, detail="Album is not registered")
    return crud.update_album(db=db, id=album_id, album=album)


@router.get("/albums", response_model=list[schemas.Album], tags=["Albums"])
def read_albums(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    albums = crud.get_albums(db, skip=skip, limit=limit)
    return albums


@router.get("/{album_name}", response_model=schemas.Album, tags=["Albums"])
def read_album(full_name: str, db: Session = Depends(get_db)):
    album = crud.get_album_by_full_name(db, full_name=full_name)
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@router.delete("/{album_id}", response_model=schemas.Album, tags=["Albums"])
def delete_album(album_id: int, db: Session = Depends(get_db)):
    album_exists = crud.get_album_by_id(db, id=album_id)
    if album_exists:
        album = crud.delete_album(db, album_id=album_id)
        return album
    else:
        raise HTTPException(status_code=404, detail="Album not found")


@router.post("/artists", response_model=schemas.Artist, tags=["Artists"])
def create_artist(artist: schemas.Artist, db: Session = Depends(get_db)):
    artist_exists = crud.get_artist_by_full_name(db, full_name=artist.full_name)
    if artist_exists:
        raise HTTPException(status_code=400, detail="Artist already registered")
    return crud.create_artist(db=db, artist=artist)


@router.put("/{artist_id}", response_model=schemas.Artist,  tags=["Artists"])
def update_artist(artist_id: str, artist: schemas.Artist, db: Session = Depends(get_db)):
    artist_exists = crud.get_artist_by_id(db, id=artist_id)
    if not artist_exists:
        raise HTTPException(status_code=400, detail="Artist is not registered")
    return crud.update_artist(db=db, id=artist_id, artist=artist)


@router.get("/artists", response_model=list[schemas.Artist], tags=["Artists"])
def read_artists(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    artists = crud.get_artists(db, skip=skip, limit=limit)
    return artists


@router.get("/{artist_name}", response_model=schemas.Artist, tags=["Artists"])
def read_artist(full_name: str, db: Session = Depends(get_db)):
    artist = crud.get_artist_by_full_name(db, full_name=full_name)
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist


@router.delete("/{artist_id}", response_model=schemas.Artist, tags=["Artists"])
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    artist_exists = crud.get_artist_by_id(db, id=artist_id)
    if artist_exists:
        artist = crud.delete_artist(db, artist_id=artist_id)
        return artist
    else:
        raise HTTPException(status_code=404, detail="Artist not found")


@router.post("/tracks", response_model=schemas.Track, tags=["Tracks"])
def create_track(track: schemas.Track, db: Session = Depends(get_db)):
    track_exists = crud.get_track_by_full_name(db, full_name=track.full_name)
    if track_exists:
        raise HTTPException(status_code=400, detail="Track already registered")
    return crud.create_track(db=db, track=track)


@router.put("/{track_id}", response_model=schemas.Track,  tags=["Tracks"])
def update_track(track_id: str, track: schemas.Track, db: Session = Depends(get_db)):
    track_exists = crud.get_track_by_id(db, id=track_id)
    if not track_exists:
        raise HTTPException(status_code=400, detail="Track is not registered")
    return crud.update_track(db=db, id=track_id, track=track)


@router.get("/tracks", response_model=list[schemas.Track], tags=["Tracks"])
def read_tracks(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    tracks = crud.get_tracks(db, skip=skip, limit=limit)
    return tracks


@router.get("/{track_name}", response_model=schemas.Track, tags=["Tracks"])
def read_track(full_name: str, db: Session = Depends(get_db)):
    track = crud.get_track_by_full_name(db, full_name=full_name)
    if track is None:
        raise HTTPException(status_code=404, detail="Track not found")
    return track


@router.delete("/{track_id}", response_model=schemas.Track, tags=["Tracks"])
def delete_track(track_id: int, db: Session = Depends(get_db)):
    track_exists = crud.get_track_by_id(db, id=track_id)
    if track_exists:
        track = crud.delete_track(db, track_id=track_id)
        return track
    else:
        raise HTTPException(status_code=404, detail="Track not found")