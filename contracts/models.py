from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from attorneys.models import Attorney
from database import Base
from ..attorneys.models import Attorney

class Contract(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    attorney = relationship(Attorney)
    # username = Column(String, unique=True, index=True)
    # email = Column(String)
    # password = Column(String)
    # is_active = Column(Boolean, default=True)
    # full_name = Column(String)
