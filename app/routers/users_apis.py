from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.services.users_svc import users_svc
from app.config import get_db
from app.services.auth_svc import oauth2_scheme
from app.schemas import UserCreate

router = APIRouter()
u_svc = users_svc()

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    result = u_svc.create_user(db, user.name, user.email, user.password)
    if result["success"]:
        return JSONResponse(status_code=201, content=result["message"])
    return JSONResponse(status_code=404, content=result["message"])

@router.post("/login")
def login(db: Session= Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    result = u_svc.login(db, form_data.username,form_data.password)
    if result["success"]:
        return JSONResponse(status_code=200,content= result)
    return JSONResponse(status_code= 404,content= result["message"])

@router.get("/")
def get_users(db: Session= Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        users= u_svc.get_users(db)
    except Exception as ex:
        return JSONResponse(status_code=404,content="No users found")
    return users
    return JSONResponse(status_code=200,content= users_data)

@router.delete("/")
def delete_user(id : int, db: Session= Depends(get_db), token: str = Depends(oauth2_scheme)):
    result = u_svc.delete_user(db, id)
    if result["success"]:
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])