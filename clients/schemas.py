from pydantic import BaseModel
from contracts import schemas

class Client(BaseModel):
    id: int
    name: str
    email: str = None
    phone: str = None
    contracts: list[schemas.Contract] = []

    class Config:
        orm_mode = True
