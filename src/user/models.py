from sqlalchemy import Column,String,Integer,Boolean,DateTime
from src.utils.db import Base

class UserModel(Base):
    __tablename__="user_table"

    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    username=Column(String,nullable=False,unique=True)
    hash_password=Column(String,nullable=False)
    email=Column(String,unique=True)