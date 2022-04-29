from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class BattlelogPlayers(Base):
    __tablename__ = "battlelog_players"

    id = Column(Integer,primary_key=True,index=True)
    tag = Column(Text,unique = True,index=True)
    name = Column(Text)
    brawler_id = Column(Integer,unique =True)
    brawler_name =Column(Text)
    brawler_power =Column(Integer)
    brawler_trophies = Column(Integer)


class Players(Base):
    __tablename__ = "players"

    tag = Column(Text,primary_key= True,index = True)
    name = Column(Text, index=True)
    last_update = Column(DateTime(timezone=False))
    name_color = Column(Text)
    icon_id = Column(Integer)
    trophies = Column(Integer)
    highest_trophies =Column(Integer)
    exp_level = Column(Integer)
    exp_points = Column(Integer)
    is_qualified_from_championship_challenge = Column(Boolean)
    the_3vs3_victories = Column(Integer)
    solo_victories = Column(Integer)
    duo_victories = Column(Integer)
    best_robo_rumble_time =Column(Integer)
    best_time_as_big_brawler = Column(Integer)
    club_tag = Column(Text)
    club_name = Column(Text)
    

def get_last_update( i: Players):
    return i.last_update

