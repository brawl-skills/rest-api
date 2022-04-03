# DATABASE CONNECTION( POSTGRE )

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_url = "postgresql://user:psword@localhost/our_db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
