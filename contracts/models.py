from sqlalchemy import ForeignKey, Column, Integer, DateTime
from database import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    attorney_id = Column(Integer, ForeignKey("attorneys.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    mortgage_applicaton_date = Column(DateTime)
