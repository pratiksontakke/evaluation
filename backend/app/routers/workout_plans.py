from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from sqlalchemy import select
from backend.app.db.database import get_session
from backend.app.models.WorkoutPlans import WorkoutPlansModel
from backend.app.schemas.WorkoutPlans import WorkoutPlansSchema
from typing import List

router = APIRouter()

@router.post("/", response_model=WorkoutPlansSchema)
def add_workout_plan(plan: WorkoutPlansSchema, db: session = Depends(get_session)):
    db_plan = WorkoutPlansModel(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

@router.get("/", response_model=List[WorkoutPlansSchema])
def get_all_workout_plans(db: session = Depends(get_session), limit: int = 10, offset: int = 0):
    plans = db.execute(select(WorkoutPlansModel).offset(offset).limit(limit)).scalars().all()
    return plans