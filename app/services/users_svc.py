from sqlalchemy.orm import Session
from app.dac.dac_pg import dac_pg


class users_svc:
    def __init__(self):
        self.dac = dac_pg()

    def get_users(self, db : Session):
        return self.dac.get_users(db)
    
    def create_user(self, db : Session, name :str ,email: str, password : str):
        if self.dac.create_user(db,name,email,password):
            return {"message": "Created user successfully", "success": True}
        return {"message": "Failed to create user", "success": False}