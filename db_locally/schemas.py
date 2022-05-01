from typing import Optional


from sqlalchemy import DATETIME
from pydantic import BaseModel
from datetime import datetime


class Trophies(BaseModel):
    brawler_trophies : int
    
    class Config:
        orm_mode = True


