from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class Post(BaseModel):
    post_id: int
    title: str
    content: str

class CreatePost(BaseModel):
    title: str
    content: str
    userid: int

class Comment(BaseModel):
    content: str

class CreateComment (BaseModel):
    userid: int
    content: str