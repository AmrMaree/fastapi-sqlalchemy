from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.services.comments_svc import comments_svc
from app.config import get_db
from app.services.auth_svc import oauth2_scheme
from app.schemas import Comment

router = APIRouter()
c_svc = comments_svc()

@router.post("/posts/{post_id}/comments")
def create_comment(post_id: int, comment: Comment, db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    result = c_svc.create_comment(db, comment.content, post_id , comment.userid)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.delete("/comments/{comment_id}")
def delete_comment(comment_id : int, db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    result = c_svc.delete_comment(db, comment_id)
    if result["success"]:
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.get("/posts/{post_id}/comments")
def get_post_comments(post_id : int, db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    comments = c_svc.get_post_comments(db, post_id)
    if comments:
        return comments
    return {"message": "No comments found"}

@router.get("/comments/{comment_id}")
def get_comment_by_id (comment_id : int, db : Session = Depends(get_db), token : str = Depends(oauth2_scheme)):
    try:
        comment = c_svc.get_comment_by_id(comment_id, db)
    except Exception as ex:
        return JSONResponse(status_code=404,content="No Comment Found")
    return comment

@router.put("/comments/{comment_id}")
def edit_comment(comment_id : int, comment : Comment, db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    result = c_svc.edit_comment(db, comment_id, comment.content)
    if result["success"]:
        return JSONResponse(status_code=200, content= result["message"])
    return JSONResponse(status_code=404, content= result["message"])
