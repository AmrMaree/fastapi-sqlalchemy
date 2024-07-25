from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.services.posts_svc import posts_svc
from app.db_pg import get_db
from app.services.auth_svc import oauth2_scheme

router = APIRouter()
p_svc = posts_svc()

@router.post("/")
def create_post(title : str, content : str, userid : int, db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    result = p_svc.create_post(db, title, content, userid)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.delete("/{post_id}")
def delete_post(id : int, db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    result = p_svc.delete_post(db, id)
    if result["success"]: 
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.get("/")
def get_posts(db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        post = p_svc.get_posts(db)
    except Exception as ex:
        return JSONResponse(status_code=404,content="No post found")
    return post
    return JSONResponse(status_code=200,content= post)