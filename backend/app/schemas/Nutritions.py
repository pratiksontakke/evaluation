from pydantic import BaseModel
from sqlalchemy import DateTime

class NutritionsSchema(BaseModel):
    id: int
    user_id: int
    date_time: DateTime
    meals: str
    calories: int
    macros: int
    
    class Config:
        orm = True
