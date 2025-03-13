from fastapi import FastAPI 
from core.database import engine 
from models import user as user_model 
from api import user as user_api 
from api import ai as ai_api

user_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title='User App')

app.include_router(user_api.router,prefix='/users',tags= ['Users'])
app.include_router(ai_api.router,prefix='/ai',tags=['AI'])
