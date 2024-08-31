from typing import List
from dotenv import load_dotenv
import uvicorn

load_dotenv()

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.config import engine
from app.routers import users_apis,posts_apis,comments_apis,search_apis
from sqlalchemy.orm import Session
from app.config import get_db
from app.models import Post

models.Base.metadata.create_all(engine)

app = FastAPI(title="My FastAPI Project", description="This is my Project's API Service") #change here

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

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

# Initialize the ConnectionManager
manager = ConnectionManager()

# Define a WebSocket endpoint to handle connections
@app.websocket("/ws/posts")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await manager.connect(websocket)
    try:
        while True:
            posts_count = db.query(Post).count()
            await manager.broadcast(str(posts_count))
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as ex:
        print(ex)


app.include_router(users_apis.router, prefix="/users",tags=["users"])
app.include_router(posts_apis.router,prefix="/posts",tags=["posts"])
app.include_router(comments_apis.router, prefix="", tags=["comments"])
app.include_router(search_apis.router, prefix="",tags=["search"])

if __name__ == "__main__":
    uvicorn.run(app, host= "0.0.0.0", port=8000)