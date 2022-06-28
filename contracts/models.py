from sqlalchemy import ForeignKey, Column, Integer, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    #attorney = relationship(Attorney)
    attorney_id = Column(Integer, ForeignKey("attorneys.id"))
    mortgage_applicaton_date = Column(DateTime)

    #attorney = relationship("Attorney", back_populates="attorney")
    # username = Column(String, unique=True, index=True)
    # email = Column(String)
    # password = Column(String)
    # is_active = Column(Boolean, default=True)
    # full_name = Column(String)
