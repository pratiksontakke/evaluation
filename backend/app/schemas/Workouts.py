from datetime import datetime
from pydantic import BaseModel

class WorkoutsSchema(BaseModel):
    id: int
    user_id: int
    plan_name: str
    date_time: datetime
    exercises: int
    duration: int
    
    class Config:
        orm = True