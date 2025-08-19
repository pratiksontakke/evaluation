from datetime import datetime
from pydantic import BaseModel

class Nutritions(BaseModel):
    id: int
    user_id: int
    date: datetime
    meals: str
    calories: int
    macros: int
    
    class Config:
        orm = True
