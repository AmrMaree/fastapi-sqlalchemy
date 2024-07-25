from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.services.users_svc import users_svc
from app.db_pg import get_db

router = APIRouter()
u_svc = users_svc()

@router.post("/")
def create_post(title : str, content : str, userid : int, db : Session = Depends(get_db)):
    result = u_svc.create_post(db, title, content, userid)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.delete("/{post_id}")
def delete_post(id : int, db : Session = Depends(get_db)):
    result = u_svc.delete_post(db, id)
    if result["success"]: 
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.get("/")
def get_posts(db : Session = Depends(get_db)):
    try:
        post = u_svc.get_posts(db)
    except Exception as ex:
        return JSONResponse(status_code=404,content="No post found")
    return post
    return JSONResponse(status_code=200,content= post)