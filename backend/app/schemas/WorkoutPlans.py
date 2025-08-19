from pydantic import BaseModel

class WorkoutPlansSchema(BaseModel):
    id: int
    user_id: int
    plan_name: str
    difficulty: str
    duration: int
    target_muscle_groups: str
    exercises_list: str
    
    class Config:
        orm = True