from sqlalchemy import Column,Integer,String 
from core.database import Base 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(length=100),index=True)
    email = Column(String(length=100),unique=True,index=True)
    