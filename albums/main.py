from . import crud, schemas
from fastapi import Depends, APIRouter, HTTPException
from dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/albums",
)

@router.post("/", response_model=schemas.Album, tags=["Albums"])
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


@router.get("/", response_model=list[schemas.Album], tags=["Albums"])
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
