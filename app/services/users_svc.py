from sqlalchemy.orm import Session
from app.dac.dac import dac

class users_svc:
    def __init__(self):
        self.dac = dac()
    
    def create_user(self, db : Session, name :str ,email: str, password : str):
        if self.dac.create_user(db,name,email,password):
            return {"message": "Created user successfully", "success": True}
        return {"message": "Failed to create user", "success": False}
    
    def login(self, db : Session, email : str, password : str):
        token = self.dac.login(db,email,password)
        if token:
            return {"message": "Logged in successfully","token":token, "success": True}
        return {"message": "Failed to login", "success": False}

    def get_users(self, db : Session):
        return self.dac.get_users(db)
    
    def delete_user(self, db : Session, id : int):
        if self.dac.delete_user(db, id):
            return {"message": "Deleted user successfully", "success": True}
        return {"message": "Failed to delete user", "success": False}
    
