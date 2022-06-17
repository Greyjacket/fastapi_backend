import datetime
from pydantic import BaseModel


class Property(BaseModel):
    id: int
    address: str
    mortgage_applicaton_date: datetime.date
    
    class Config:
        orm_mode = True