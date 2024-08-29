from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.config import get_db
from app.services.auth_svc import oauth2_scheme
from app.services.search_svc import search_svc


router = APIRouter()
s_svc = search_svc()

@router.get("/users/{search_query}")
def search_users(search_query : str, db: Session = Depends(get_db), token : str = Depends(oauth2_scheme)):
    try:
        users = s_svc.search_users(db, search_query)
    except Exception as ex:
        return JSONResponse(status_code=404,content="No users found")
    return users

@router.get("/posts/{search_query}")
def search_posts(search_query : str, db: Session = Depends(get_db), token : str = Depends(oauth2_scheme)):
    try:
        posts = s_svc.search_posts(db, search_query)
    except Exception as ex:
        return JSONResponse(status_code=404,content="No posts found")
    return posts