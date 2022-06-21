from pydantic import BaseModel


class Agent(BaseModel):
    id: int
    name: str
    phone: str
    organization: str
    
    class Config:
        orm_mode = True