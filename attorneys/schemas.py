from pydantic import BaseModel
from contracts import schemas

class Attorney(BaseModel):
    id: int
    name: str
    phone: str
    contracts: list[schemas.Contract] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True