from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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

if __name__ == "__main__":
    uvicorn.run(app, host= "0.0.0.0", port=8000)