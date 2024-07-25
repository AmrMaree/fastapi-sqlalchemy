from sqlalchemy.orm import Session
from app import models
from app.utils.utils import utils
from app.services import auth_svc

class dac:
    def __init__(self):
        pass

    def create_user(self, db:Session, name :str ,email: str, password : str):
        try:
            hashed_password,salt = utils.hash_password_sign_up(password)
            user = models.User(name=name,email=email,password=hashed_password,salt=salt)
            db.add(user)
            db.commit()
            db.refresh(user)
        except Exception as ex:
            print("Failed to create user")
            raise ex
        return user
    
    def login(self, db : Session, email : str, password : str):
        try:
            result = db.query(models.User).filter(models.User.email == email).first()
            hashed_password= result.password
            salt = bytes.fromhex(result.salt)
            login_password = utils.hash_password_login(password,salt)
            if login_password == hashed_password:
                print("Login successful")
                token = auth_svc.encode_auth_token(email)
                print(salt)
                return token
            else:
                print("Incorrect password")
                print(salt)
                return False
        except Exception as ex:
            print("Failed to login")
            raise ex
    
    def get_users(self, db: Session):
        return db.query(models.User).all()
    
    def delete_user(self, db : Session, id : int):
        try:
            user= db.query(models.User).filter(models.User.id == id).first()
            if user:
                db.delete(user)
                db.commit()
                return True
            return False
        except Exception as ex:
            print("Failed to delete user")
            raise ex

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
    
    def create_comment(self, db : Session, content : str, post_id: int, user_id : int):
        try:
            comment= models.Comment(content=content,post_id=post_id,user_id=user_id)
            db.add(comment)
            db.commit()
            db.refresh(comment)
        except Exception as ex:
            print("Failed to create a new comment")
            raise ex
        return comment
    
    def get_post_comments(self, db : Session, post_id : int):
        return db.query(models.Comment).filter(models.Comment.post_id == post_id).all() 
    
    def delete_comment(self, db : Session, id : int):
        try:
            comment= db.query(models.Comment).filter(models.Comment.id == id).first()
            if comment:
                db.delete(comment)
                db.commit()
                return True
            return False
        except Exception as ex:
            print("Failed to delete comment")
            raise ex