from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Property(Base):
    __tablename__ = "properties"
    
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    owner_id = Column(Integer, ForeignKey("clients.id"))
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    contracts = relationship("Contract", backref="property_contracts")
