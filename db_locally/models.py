from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class BattlelogPlayers(Base):
    __tablename__ = "battlelog_players"

    id = Column(Integer,primary_key=True,index=True)
    tag = Column(Text,unique = True,index=True)
    name = Column(String)
    brawler_id = Column(Integer,unique =True)
    brawler_name =Column(String)
    brawler_power =Column(Integer)
    brawler_trophies = Column(Integer)



