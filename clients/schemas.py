from pydantic import BaseModel, validator
from contracts import schemas

class Client(BaseModel):
    id: int
    first_name: str
    last_name: str
    full_name: str = None
    email: str = None
    phone: str = None
    contracts: list[schemas.Contract] = []

    class Config:
        orm_mode = True

    @validator('full_name')
    def create_full_name(cls,full_name, values):
        full_name = values['first_name'] + " " + values['last_name']
        return full_name