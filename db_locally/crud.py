from sqlalchemy.orm import Session
from . import models


def get_player_trophies(db:Session,player_id:int):
    return db.query(models.BattlelogPlayers).filter(models.BattlelogPlayers.id == player_id).first()


def get_players_info(db:Session):
    return db.query(models.Players).all()


def get_players_brawlers_gears(db:Session):
    return db.query(models.PlayersBrawlersGears).all()


def get_battlelogs(db:Session):
    return db.query(models.Battlelogs).all()
