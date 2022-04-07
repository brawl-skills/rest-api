from sqlalchemy.orm import Session

from . import models, schemas


def get_player(db: Session, player_id:str):
    return db.query(models.PlayerInfo).filter(models.PlayerInfo.id == player_id).first()


def get_player_by_name(db: Session, player_name: str):
    return db.query(models.PlayerInfo).filter(models.PlayerInfo.name == player_name).first()


def get_players(db: Session, skip:int = 0, limit: int =100):
    return db.query(models.PlayerInfo).offset(skip).limit(limit).all()


def get_statistics(db: Session, skip:int=0, limit:int=100):
    return db.query(models.Statistics).offset(skip).limit(limit).all()


def create_player(db: Session , player: schemas.PlayerCreate):
    #hashed_pass = player.password + "hashed"
    db_player =models.PlayerInfo(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def create_statistics(db: Session, statistic: schemas.StatisticsCreate,player_id:str):
    db_statistic = models.Statistics(**statistic.dict(),tag= player_id)
    db.add(db_statistic)
    db.commit()
    db.refresh(db_statistic)
    return db_statistic