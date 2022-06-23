from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
#from attorneys.models import Attorney
from database import Base
#from ..attorneys.models import Attorney

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    #attorney = relationship(Attorney)
    attorney_id = Column(Integer, ForeignKey("attorneys.id"))
    # username = Column(String, unique=True, index=True)
    # email = Column(String)
    # password = Column(String)
    # is_active = Column(Boolean, default=True)
    # full_name = Column(String)
