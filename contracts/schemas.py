from pydantic import BaseModel


class Contract(BaseModel):
    id: int
    attorney_id: int
    client_id: int

    class Config:
        orm_mode = True
