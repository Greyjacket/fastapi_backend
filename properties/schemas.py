from pydantic import BaseModel
from contracts import schemas


class Property(BaseModel):
    id: int
    address: str
    contracts: list[schemas.Contract] = []

    class Config:
        orm_mode = True