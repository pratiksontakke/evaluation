from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import Session

engine = engine = create_engine("sqlite:////home/pratik/misogiai/evaluation/backend/app/sqliteDB/gym.db")

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    Base.metadata.create_all(engine)

class Base(DeclarativeBase):
    pass
