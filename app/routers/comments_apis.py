from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.services.comments_svc import comments_svc
from app.db_pg import get_db

router = APIRouter()
c_svc = comments_svc()

@router.post("/posts/{id}/comments")
def create_comment(content : str, post_id: int, user_id : int, db : Session = Depends(get_db)):
    result = c_svc.create_comment(db, content, post_id ,user_id)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.delete("/comments/{comment_id}")
def delete_comment(id : int, db : Session = Depends(get_db)):
    result = c_svc.delete_comment(db, id)
    if result["success"]: 
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.get("/posts/{id}/comments")
def get_post_comments(post_id : int, db : Session = Depends(get_db)):
    comments = c_svc.get_post_comments(db, post_id)
    if comments:
        return comments
    return {"message": "No comments found"}
