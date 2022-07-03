from pydantic import BaseModel
from contracts import schemas
 

class Agent(BaseModel):
    id: int
    name: str
    phone: str
    organization: str
    contracts: list[schemas.Contract] = []

    class Config:
        orm_mode = True