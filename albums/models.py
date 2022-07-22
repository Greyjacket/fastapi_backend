from sqlalchemy import ForeignKey, Column, Integer, DateTime, String
from sqlalchemy.orm import relationship
from database import Base


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    track_number = Column(Integer)
    agents_id = Column(Integer, ForeignKey("albums.id"))

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
    tracks = relationship("Track", backref="track_album")
