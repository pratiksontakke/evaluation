from datetime import datetime
from pydantic import BaseModel

class ProgressSchema(BaseModel):
    id: int
    user_id: int
    workout_id: int
    sets: int
    reps: int
    weight: int
    notes: str
    
    class Config:
        orm = True