from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class Post(BaseModel):
    title: str
    content: str

class CreatePost(BaseModel):
    title: str
    content: str
    userid: int