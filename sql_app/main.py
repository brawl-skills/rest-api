from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud , schemas, models
from .database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/players/", response_model=schemas.Player)
async def create_player (player:schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player =crud.get_player_by_name(db=db,player=player)
    if db_player:
        raise HTTPException(status_code=400, detail = "Name already registered")
    return crud.create_player(db=db,player=player)
