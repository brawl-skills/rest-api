from fastapi import FastAPI, HTTPException, Depends, Request, Response
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models,crud,schemas
from .database import SessionLocal, engine
import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Getting the number of trophies of a player

@app.get("/trophies/{player_id}", response_model = schemas.Trophies)
async def get_player_trophies(player_id:int,db:Session = Depends(get_db)):
    trophies = crud.get_player_trophies(db,player_id=player_id)
    if trophies is None:
        raise HTTPException(status_code=404,detail="Player not found")
    return trophies


# Getting the number of players online(at least 15 min ago)

@app.get("/number_of_players_online/")
async def number_of_players_online(db:Session = Depends(get_db)):
    players = crud.get_all_last_updates(db)
    # initialisation to  zero of the number of players online
    number : int = 0
    # at least delta t = 15 min
    delta_t = datetime.timedelta(minutes=15)
    
    for info in players:
        last_update = models.get_last_update(info)
        delta = datetime.datetime.now() - last_update
        

        if delta < delta_t:
            number += 1

    return {"Количество игроков онлайн  " : number }



