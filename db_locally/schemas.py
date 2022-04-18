from typing import Optional
from pydantic import BaseModel


class Trophies(BaseModel):
    brawler_trophies : int
    
    class Config:
        orm_mode = True