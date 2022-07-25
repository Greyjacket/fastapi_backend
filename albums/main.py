from . import crud, schemas
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/music",
)

@router.post("/albums", response_model=schemas.Album, tags=["Albums"])
def create_album(album: schemas.Album, db: Session = Depends(get_db)):
    album_exists = crud.get_album_by_title(db, title=album.title)
    if album_exists:
        raise HTTPException(status_code=400, detail="Album already registered")
    return crud.create_album(db=db, album=album)


@router.put("/albums/{album_id}", response_model=schemas.Album,  tags=["Albums"])
def update_album(album_id: str, album: schemas.Album, db: Session = Depends(get_db)):
    album_exists = crud.get_album_by_id(db, id=album_id)
    if not album_exists:
        raise HTTPException(status_code=400, detail="Album is not registered")
    return crud.update_album(db=db, id=album_id, album=album)


@router.get("/albums", response_model=list[schemas.Album], tags=["Albums"])
def read_albums(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    albums = crud.get_albums(db, skip=skip, limit=limit)
    return albums


@router.get("/albums/{album_name}", response_model=schemas.Album, tags=["Albums"])
def read_album(title: str, db: Session = Depends(get_db)):
    album = crud.get_album_by_title(db, title=title)
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@router.delete("/albums/{album_id}", response_model=schemas.Album, tags=["Albums"])
def delete_album(album_id: int, db: Session = Depends(get_db)):
    album_exists = crud.get_album_by_id(db, id=album_id)
    if album_exists:
        album = crud.delete_album(db, album_id=album_id)
        return album
    else:
        raise HTTPException(status_code=404, detail="Album not found")


@router.post("/artists", response_model=schemas.Artist, tags=["Artists"])
def create_artist(artist: schemas.Artist, db: Session = Depends(get_db)):
    artist_exists = crud.get_artist_by_full_name(db, name=artist.name)
    if artist_exists:
        raise HTTPException(status_code=400, detail="Artist already registered")
    return crud.create_artist(db=db, artist=artist)


@router.put("/artists/{artist_id}", response_model=schemas.Artist,  tags=["Artists"])
def update_artist(artist_id: str, artist: schemas.Artist, db: Session = Depends(get_db)):
    artist_exists = crud.get_artist_by_id(db, id=artist_id)
    if not artist_exists:
        raise HTTPException(status_code=400, detail="Artist is not registered")
    return crud.update_artist(db=db, id=artist_id, artist=artist)


@router.get("/artists", response_model=list[schemas.Artist], tags=["Artists"])
def read_artists(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    artists = crud.get_artists(db, skip=skip, limit=limit)
    return artists


@router.get("/artists/{artist_name}", response_model=schemas.Artist, tags=["Artists"])
def read_artist(name: str, db: Session = Depends(get_db)):
    artist = crud.get_artist_by_full_name(db, name=name)
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist


@router.delete("/artists/{artist_id}", response_model=schemas.Artist, tags=["Artists"])
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    artist_exists = crud.get_artist_by_id(db, id=artist_id)
    if artist_exists:
        artist = crud.delete_artist(db, artist_id=artist_id)
        return artist
    else:
        raise HTTPException(status_code=404, detail="Artist not found")


@router.post("/tracks", response_model=schemas.Track, tags=["Tracks"])
def create_track(track: schemas.Track, db: Session = Depends(get_db)):
    track_exists = crud.get_track_by_title(db, title=track.title)
    if track_exists:
        raise HTTPException(status_code=400, detail="Track already registered")
    return crud.create_track(db=db, track=track)


@router.put("/tracks/{track_id}", response_model=schemas.Track,  tags=["Tracks"])
def update_track(track_id: str, track: schemas.Track, db: Session = Depends(get_db)):
    track_exists = crud.get_track_by_id(db, id=track_id)
    if not track_exists:
        raise HTTPException(status_code=400, detail="Track is not registered")
    return crud.update_track(db=db, id=track_id, track=track)


@router.get("/tracks", response_model=list[schemas.Track], tags=["Tracks"])
def read_tracks(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    tracks = crud.get_tracks(db, skip=skip, limit=limit)
    return tracks


@router.get("/tracks/{track_name}", response_model=schemas.Track, tags=["Tracks"])
def read_track(title: str, db: Session = Depends(get_db)):
    track = crud.get_track_by_title(db, title=title)
    if track is None:
        raise HTTPException(status_code=404, detail="Track not found")
    return track


@router.delete("/tracks/{track_id}", response_model=schemas.Track, tags=["Tracks"])
def delete_track(track_id: int, db: Session = Depends(get_db)):
    track_exists = crud.get_track_by_id(db, id=track_id)
    if track_exists:
        track = crud.delete_track(db, track_id=track_id)
        return track
    else:
        raise HTTPException(status_code=404, detail="Track not found")