from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    password: str

class EditUser(BaseModel):
    name: str
    email: EmailStr
    role: str

class Post(BaseModel):
    post_id: Optional[int] = None
    title: str
    content: str

class CreatePost(BaseModel):
    title: str
    content: str
    userid: int

class Comment(BaseModel):
    userid: Optional[int] = None
    content: str