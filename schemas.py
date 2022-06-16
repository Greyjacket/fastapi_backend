import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str | None
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class Property(BaseModel):
    id: int
    address: str
    mortgage_applicaton_date: datetime.date
    
    class Config:
        orm_mode = True