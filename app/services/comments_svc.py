from sqlalchemy.orm import Session
from app.dac.dac import dac

class comments_svc:
    def __init__(self):
        self.dac = dac()

    def create_comment(self, db : Session, content : str, post_id : int, user_id : int):
        if self.dac.create_comment(db, content, post_id, user_id):
            return {"message": "Created comment successfully", "success": True}
        return {"message": "Failed to create comment", "success": False}

    def get_post_comments(self, db : Session, post_id : int):
        return self.dac.get_post_comments(db, post_id)

    def delete_comment(self, db : Session, id : int):
        if self.dac.delete_comment(db, id):
            return {"message": "Deleted comment successfully", "success": True}
        return {"message": "Failed to delete comment", "success": False}
    
    def edit_comment(self, db : Session, comment_id : int, content : str):
        if self.dac.edit_comment(db, comment_id, content):
            return {"message": "Edited comment successfully", "success": True}
        return {"message": "Failed to edit comment", "success": False}
    
    def get_comment_by_id(self, id : int, db : Session):
        return self.dac.get_comment_by_id(id, db)
