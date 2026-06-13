from pydantic import BaseModel

class UserCreate(BaseModel):
    fullname: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    fullname: str
    email: str

    class Config:
        from_attributes = True