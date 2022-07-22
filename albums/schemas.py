from pydantic import BaseModel, validator
import datetime

class Track(BaseModel):
    id: int
    title: str
    track_number: int
    album_id: int
    artist_id: int

    class Config:
        orm_mode = True


class Album(BaseModel):
    id: int
    title: str
    artist_id: int
    format: str
    total_tracks: int
    release_date: datetime = None
    purchase_data: datetime = None
    date_added: datetime
    track: list[Track] = []

    class Config:
        orm_mode = True

class Artist(BaseModel):
    id: int
    name: str
    format: str
    total_tracks: int
    release_date: datetime = None
    purchase_data: datetime = None
    date_added: datetime
    track: list[Track] = []

    class Config:
        orm_mode = True