from pydantic import BaseModel, validator
from datetime import date

class Track(BaseModel):
    id: int
    title: str
    track_number: int
    length: int
    album_id: int = None
    artist_id: int = None
    date_added: date

    class Config:
        orm_mode = True


class Album(BaseModel):
    id: int
    title: str
    artist_id: int
    format: str
    total_tracks: int
    release_date: date = None
    purchase_date:date = None
    date_added: date
    tracks: list[Track] = []

    class Config:
        orm_mode = True


class Artist(BaseModel):
    id: int
    name: str
    date_added: date = None
    tracks: list[Track] = []
    albums: list[Album] = []

    class Config:
        orm_mode = True