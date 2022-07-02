from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String, unique=True)
    contracts = relationship("Contract", backref="client_contracts")
