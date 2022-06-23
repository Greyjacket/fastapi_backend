from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
#from contracts import models

class Attorney(Base):
    __tablename__ = "attorneys"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
    #contract_id = Column(Integer, ForeignKey())
    contract = relationship("Contract")