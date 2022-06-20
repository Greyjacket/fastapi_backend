from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Attorney(Base):
    __tablename__ = "attorneys"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
