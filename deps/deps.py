from core.database import SessionLocal
from sqlalchemy.orm import Session 

def get_db():
    db = SessionLocal()
    try : 
        yield db 
    except Exception as err:
        print(f'error in getting db : {err}')
    finally:
        db.close()