from sqlalchemy import ForeignKey, Column, Integer, DateTime, String
from sqlalchemy.orm import relationship
from database import Base


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    track_number = Column(Integer)
    artist_id = Column(Integer, ForeignKey("artist.id"))
    album_id = Column(Integer, ForeignKey("albums.id"))

    class Config:
        orm_mode = True
        
class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    artist: Column(String)
    format: Column(String)
    total_tracks: Column(Integer)
    release_date: Column(DateTime)
    purchase_data: Column(DateTime)
    date_added: Column(DateTime)
    artist_id = Column(Integer, ForeignKey("artist.id"))
    tracks = relationship("Track", backref="track_album")

    class Config:
        orm_mode = True

class Artist(Base):
    __tablename__ = "artists"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    format: Column(String)
    date_added: Column(DateTime)
    tracks = relationship("Track", backref="artist_tracks")
    albums = relationship("Album", backref="artist_albums")

    class Config:
        orm_mode = True