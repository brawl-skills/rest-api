from sqlachemy import Boolean



from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class PlayerInfo(Base):
    __tablename__ = "players"

    id = Column(String, primary_key=True, index= True)
    name = Column(String, index = True)
    age = Column(Integer)
    personage = Column(String)
    is_active = Column(Boolean, default=True)

    statistics = relationship("Statistics", back_populates ="")


class Statistics(Base):
    __tablename__ = "statistics"

    rank = Column(Integer, primary_key= True,index = True)
    level = Column(Integer)
    name = Column(String)
    tag = Column(String, ForeignKey("players.id"))

    relation = relationship("Player",back_populates="statistics")