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
    
    def create_post(self, db : Session, title : str, content : str, userid : int):
        try:
            post= models.Post(title=title,content=content,user_id=userid)
            db.add(post)
            db.commit()
            db.refresh(post)
        except Exception as ex:
            print("Failed to create a new post")
            raise ex
        return post

    def delete_post(self, db : Session, id : int):
        try:
            post= db.query(models.Post).filter(models.Post.id == id).first()
            if post:
                db.delete(post)
                db.commit()
                return True
            return False
        except Exception as ex:
            print("Failed to delete post")
            raise ex

    def get_posts(self, db : Session):
        return db.query(models.Post).all()

    