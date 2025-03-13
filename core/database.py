from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker,declarative_base 

from .config import DATABASE_URI

engine = create_engine(DATABASE_URI,pool_pre_ping=True)

SessionLocal = sessionmaker (autocommit=False,bind=engine)

Base = declarative_base()
