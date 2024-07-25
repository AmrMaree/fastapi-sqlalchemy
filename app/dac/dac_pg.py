from sqlalchemy.orm import Session
from app import models

class dac_pg:
    def __init__(self):
        pass

    def get_users(self, db: Session):
        return db.query(models.User).all()
    
    def create_user(self, db:Session, name :str ,email: str, password : str):
        try:
            user = models.User(name=name,email=email,password=password,salt='somesalt')
            db.add(user)
            db.commit()
            db.refresh(user)
        except Exception as ex:
            print("Failed to create user")
            raise ex
        return user

    