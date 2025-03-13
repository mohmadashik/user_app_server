from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session 
from typing import List 

from schemas import user as user_schema 
# from user_app_server.crud.user import create_user,get_users,get_user
from crud import user as user_crud
from deps import deps

router = APIRouter()

@router.post('/',response_model=user_schema.UserRead)
def create_user(user:user_schema.UserCreate,db:Session=Depends(deps.get_db)):
    print('entering create user ')
    return user_crud.create_user(db,user)

@router.get('/',response_model=List[user_schema.UserRead])
def read_users(skip:int=0,limit:int=10,db:Session=Depends(deps.get_db)):
    print(f'entering read_users , skip : {skip}, limit : {limit}')
    return user_crud.get_users(db,skip,limit)

@router.get('/{user_id}',response_model=user_schema.UserRead)
def get_user(user_id:int,db:Session=Depends(deps.get_db)):
    print(f'enter get_user , user_id : {user_id}')
    user_obj =  user_crud.get_user(db,user_id)
    if user_obj is None: 
        raise HTTPException(status_code=404,detail="User Not Found")
    return user_obj 



