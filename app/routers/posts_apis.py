from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.services.posts_svc import posts_svc
from app.config import get_db
from app.services.auth_svc import oauth2_scheme
from app.schemas import Post

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

@router.get("/{post_id}")
def get_post_by_id (post_id : int, db : Session = Depends(get_db), token : str = Depends(oauth2_scheme)):
    try:
        post = p_svc.get_post_by_id(post_id, db)
    except Exception as ex:
        return JSONResponse(status_code=404,content="No post found")
    return post

@router.put("/{post_id}")
def edit_post(post_id : int, post : Post, db : Session = Depends(get_db), token : str = Depends(oauth2_scheme)):
    result = p_svc.edit_post(db, post_id,post.title,post.content)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])
