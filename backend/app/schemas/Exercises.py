from pydantic import BaseModel

class ExercisesSchema(BaseModel):
    id: int
    name: str
    category: str
    equipment: str
    difficulty: str
    instructions: str
    target_muscles: str

    class Config:
        orm = True