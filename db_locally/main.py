from fastapi import FastAPI, HTTPException, Depends, Request, Response
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models,crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Getting the number of trophies of a player

@app.get("/trophies/{player_id}")
async def get_player_trophies(player_id:int,db:Session = Depends(get_db)):
    trophies = crud.get_player_trophies(db,player_id=player_id)
    if trophies is None:
        raise HTTPException(status_code=404,detail="Player not found")
    return trophies
