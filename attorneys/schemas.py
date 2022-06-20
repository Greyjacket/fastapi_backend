from pydantic import BaseModel


class Attorney(BaseModel):
    id: int
    name: str
    phone: str

    class Config:
        orm_mode = True