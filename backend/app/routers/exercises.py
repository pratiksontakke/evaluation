from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import session
from sqlalchemy import select
from backend.app.db.database import get_session
from backend.app.models.Exercises import ExercisesModel
from backend.app.schemas.Exercises import ExercisesSchema
from typing import List

router = APIRouter()

@router.post("/")
def add_exercise(exercise: ExercisesSchema, db: session = Depends(get_session)):
    db_exercise = ExercisesModel(**exercise.dict())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

@router.get("/", response_model=List[ExercisesSchema])
def get_all_exercises(
    db: session = Depends(get_session), 
    limit: int = 10, 
    offset: int = 0
):
    exercises = db.execute(select(ExercisesModel).offset(offset).limit(limit)).scalars().all()
    return exercises