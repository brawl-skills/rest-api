from typing import Optional
from pydantic import BaseModel


class StatisticsBase(BaseModel):
    level: str
    name: Optional[str] = None


class StatisticsCreate(StatisticsBase):
    pass


class Statistics(StatisticsBase):
    rank : int
    tag: str

    class Config:
        orm_mode =True


class PlayerBase(BaseModel):
    name: str
    personage:str


class PlayerCreate(PlayerBase):
    password: str
    age:int


class Player(PlayerBase):
    id:int
    is_active:bool
    statistics: list[Statistics]=[]

    class Congig:
        orm_mode = True