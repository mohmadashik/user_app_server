from sqlalchemy.orm import Session 
from models.user import User 
from schemas import user as user_schema 


def get_user(db:Session,user_id:int):
    return db.query(User).filter(User.id==user_id).first()

def get_users(db:Session,skip:int=0,limit:int=10):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db:Session,user:user_schema.UserCreate):
    db_user = User(name=user.name,email = user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user 

