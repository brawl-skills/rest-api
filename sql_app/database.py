from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://renata:123456@localhost:3000/test_db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocoomit = False, autoflush= False,bind =engine)

Base = declarative_base()



