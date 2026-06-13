from fastapi import FastAPI

from app.database import Base, engine
from app.routers.users import router as user_router



app = FastAPI(
    title="ISP Management API"
)

app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message": "API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }