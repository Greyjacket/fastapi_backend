from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    full_name = Column(String)
