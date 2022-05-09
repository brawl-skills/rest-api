from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True