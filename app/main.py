from fastapi import FastAPI

from app.database import Base, engine
from app.routers.users import router as user_router
from sqlalchemy import text



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
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "database connected"}
    except Exception as e:
        return {"status": "database error", "detail": str(e)}