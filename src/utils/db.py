from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.utils.settings import settings

Base=declarative_base()


engin=create_engine(url=settings.DB_CON)

LocalSession=sessionmaker(bind=engin)

def get_db():
    session=LocalSession()
    try:
        yield session
    
    finally:
        session.close()
