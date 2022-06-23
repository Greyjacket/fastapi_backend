from pydantic import BaseModel


class Contract(BaseModel):
    id: int
    attorney: int

    class Config:
        orm_mode = True