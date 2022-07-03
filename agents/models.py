from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Agent(Base):
    __tablename__ = "agents"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
    organization = Column(String)
    contracts = relationship("Contract", backref="agent_contracts")
