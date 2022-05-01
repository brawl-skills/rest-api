from fastapi import FastAPI, HTTPException, Depends, Request, Response
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import distributions, models,crud,schemas
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

@app.get("/Number_of_players_online/")
async def number_of_players_online(db:Session = Depends(get_db)):
    players = crud.get_players_info(db)
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



# Players distribution by game levels

@app.get("/Players distribution by game levels/")
async def player_distribution(db:Session= Depends(get_db)):
    player_info = crud.get_players_brawlers_gears(db)
    players_distribution_array = [0]*10
    # print(type(player_info))
    for info in player_info:
        level = int(models.get_levels(info))  #getting the level of a player
        #print(players_distribution())
        #print(level)
        distributions.player_distribution(level,players_distribution_array)
        #print(players_distribution_array)

    
    #print(players_distribution_array)
    distribution_results = distributions.level_distribution_result_schema(10,players_distribution_array)
    
    return distribution_results



# Number of battles averaged per hour over the last 24 hours

@app.get("/Battles distribution per hour/")
async def battles_distribution(db:Session = Depends(get_db)):
    battlelogs_distribution_array = [0]*12
    all_battlelogs = crud.get_battlelogs(db)
    for battlelog in all_battlelogs:
        battle_time = models.get_battle_time(battlelog)
        distributions.battlelogs_distribution(battle_time,battlelogs_distribution_array)
    
    distribution_result = distributions.battles_distribution_result_schema(12, battlelogs_distribution_array)
    return distribution_result