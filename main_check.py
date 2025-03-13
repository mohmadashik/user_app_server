from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return 'Hellooow Ashik'


@app.get('/user/{user_id}')
def read_user(user_id:int):
    return {"user" : user_id}


@app.get('/search/')
def search_query(q:str='example'):
    return {'query':q}

# fast api is fast to develop
# includes inbuilt data validation
# in built documentation support at /docs /redoc
# fast running performance
# less time to write code, few bugs
# pip3 install fastapi
# pip3 install uvicorn
# uvicorn main:app --reload
# released in 2018
# gaining popularity now a days