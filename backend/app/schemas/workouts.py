from datetime import datetime
from pydantic import BaseModel

class Workouts(BaseModel):
    id: int
    user_id: int
    plan_name: str
    date: datetime
    exercises: int
    duration: int
    
    class Config:
        orm = True