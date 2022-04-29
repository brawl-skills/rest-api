from sqlalchemy.orm import Session
from . import models


def get_player_trophies(db:Session,player_id:int):
    return db.query(models.BattlelogPlayers).filter(models.BattlelogPlayers.id == player_id).first()

def get_all_last_updates(db:Session):
    return db.query(models.Players).all()