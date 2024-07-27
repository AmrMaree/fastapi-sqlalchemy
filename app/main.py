from dotenv import load_dotenv
import uvicorn

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.config import engine
from app.routers import users_apis,posts_apis,comments_apis

models.Base.metadata.create_all(engine)

app = FastAPI(title="My FastAPI Project", description="This is my Project's API Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/",tags=["default"])
def root():
    return {"message":"Welcome to FastAPI"}

app.include_router(users_apis.router, prefix="/users",tags=["users"])
app.include_router(posts_apis.router,prefix="/posts",tags=["posts"])
app.include_router(comments_apis.router, prefix="", tags=["comments"])

if __name__ == "__main__":
    uvicorn.run(app, host= "0.0.0.0", port=8000)