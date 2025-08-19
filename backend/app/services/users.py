from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import orm

class Users(BaseModel):
    id: int
    username: str
    email: int
    password: str
    age: int
    weight: int
    height: int
    goals: str

    class Config:
        orm = True

        
