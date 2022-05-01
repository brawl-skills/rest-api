from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, DATETIME,ARRAY
from sqlalchemy.orm import relationship

from .database import Base


class BattlelogPlayers(Base):
    __tablename__ = "battlelog_players"

    id = Column(Integer,primary_key=True, index=True)
    tag = Column(Text, unique=True, index=True)
    name = Column(Text)
    brawler_id = Column(Integer, unique=True)
    brawler_name = Column(Text)
    brawler_power = Column(Integer)
    brawler_trophies = Column(Integer)


class Players(Base):
    __tablename__ = "players"

    tag = Column(Text, primary_key=True, index=True)
    name = Column(Text, index=True)
    last_update = Column(DateTime(timezone=False))
    name_color = Column(Text)
    icon_id = Column(Integer)
    trophies = Column(Integer)
    highest_trophies = Column(Integer)
    exp_level = Column(Integer)
    exp_points = Column(Integer)
    is_qualified_from_championship_challenge = Column(Boolean)
    the_3vs3_victories = Column(Integer)
    solo_victories = Column(Integer)
    duo_victories = Column(Integer)
    best_robo_rumble_time = Column(Integer)
    best_time_as_big_brawler = Column(Integer)
    club_tag = Column(Text)
    club_name = Column(Text)
    

def get_last_update(i: Players):
    return i.last_update



class PlayersBrawlersGears(Base):
    __tablename__ = "players_brawlers_gears"

    player_tag = Column(Text, primary_key=True, index=True)
    brawler_id = Column(Integer, primary_key=True, index=True)
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    lvl = Column(Integer)
    

def get_levels(i: PlayersBrawlersGears):
    return i.lvl


class Battlelogs(Base):
    __tablename__ = "battlelogs"

    id = Column(Integer, primary_key=True)
    battle_time = Column(DateTime(timezone=False))
    event_id = Column(Integer)
    event_mode = Column(Text)
    event_map = Column(Text)
    battle_mode = Column(Text)
    battle_type = Column(Text)
    battle_result = Column(Text)
    battle_duration = Column(Integer)
    battle_trophy_change = Column(Integer)
    star_pl_id = Column(Integer)
    teams = Column(ARRAY(Integer))


def get_battle_time(i: Battlelogs):
    return i.battle_time
