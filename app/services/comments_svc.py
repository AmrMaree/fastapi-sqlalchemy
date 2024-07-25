from sqlalchemy.orm import Session
from app.dac.dac_pg import dac_pg

class comments_svc:
    def __init__(self):
        self.dac = dac_pg()

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
