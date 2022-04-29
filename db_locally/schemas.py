from typing import Optional
from unittest.util import strclass

from sqlalchemy import DATETIME
from pydantic import BaseModel
from datetime import datetime


class Trophies(BaseModel):
    brawler_trophies : int
    
    class Config:
        orm_mode = True
