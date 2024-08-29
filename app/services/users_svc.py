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
        token,user_id = self.dac.login(db,email,password)
        if token:
            return {"message": "Logged in successfully","userId": user_id, "token":token, "success": True}
        return {"message": "Failed to login", "success": False}

    def get_users(self, db : Session):
        return self.dac.get_users(db)
    
    def delete_user(self, db : Session, id : int):
        if self.dac.delete_user(db, id):
            return {"message": "Deleted user successfully", "success": True}
        return {"message": "Failed to delete user", "success": False}
    
    def get_user_by_id(self, id : int, db : Session):
        return self.dac.get_user_by_id(id, db)
    
    def edit_user(self, db : Session, user_id : int , name : str, email : str, role : str):
        if self.dac.edit_user(db, user_id, name, email, role):
            return {"message": "Edited user successfully", "success": True}
        return {"message": "Failed to edit user", "success": False}
    
