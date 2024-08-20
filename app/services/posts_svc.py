from sqlalchemy.orm import Session
from app.dac.dac import dac

class posts_svc:
    def __init__(self):
        self.dac = dac()

    def create_post(self, db : Session, title : str, content : str, userid : int):
        if self.dac.create_post(db, title , content , userid):
            return {"message": "Created post successfully", "success": True}
        return {"message": "Failed to create post", "success": False}
    
    def edit_post(self, db : Session, post_id : int , title: str, content : str):
        if self.dac.edit_post(db, post_id, title, content):
            return {"message": "Edited post successfully", "success": True}
        return {"message": "Failed to edit post", "success": False}
    
        
    def delete_post(self, db : Session, id : int):
        if self.dac.delete_post(db, id):
            return {"message": "Deleted post successfully", "success": True}
        return {"message": "Failed to delete post", "success": False}
    
    def get_posts(self ,db : Session):
        return self.dac.get_posts(db)
    
    def get_post_by_id(self, id : int, db : Session):
        return self.dac.get_post_by_id(id, db)