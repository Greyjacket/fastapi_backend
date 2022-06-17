from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    full_name = Column(String)
