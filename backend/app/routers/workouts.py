from fastapi import APIRouter, Depends
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import session
from backend.app.db.database import get_session
from backend.app.models.Workouts import WorkoutsModel
from backend.app.schemas.Workouts import WorkoutsSchema

router = APIRouter();

@router.get("/") 
def get_all_workouts(db: session = Depends(get_session())) -> list[WorkoutsSchema]:
    return db.scalars(select(WorkoutsModel))

@router.get("/{workouts_id}") 
def get_workout(workouts_id, db: session = Depends(get_session())) -> WorkoutsSchema:
    return db.scalars(select(WorkoutsModel).where(WorkoutsModel.id == workouts_id)).one()

@router.post("/") 
def add_user(postWorkout : WorkoutsSchema, db: session = Depends(get_session())) -> WorkoutsSchema:
    db.add(postWorkout);
    db.commit()
    obj = db.refresh()
    db.close()
    return obj

@router.put("/{workouts_id}") 
def add_user(postWorkout : WorkoutsSchema, workouts_id, db: session = Depends(get_session())) -> WorkoutsSchema:
        db.insert(WorkoutsModel).where(WorkoutsModel.id == workouts_id).values(WorkoutsModel.plan_name==postWorkout.plan_name, 
            WorkoutsModel.date_time==postWorkout.date_time, WorkoutsModel.exercises==postWorkout.exercises, WorkoutsModel.duration==postWorkout.duration)
        db.commit()
        db.refresh()
        db.close()
        return postWorkout

@router.delete("/{workouts_id}") 
def delete_user(workouts_id, db: session = Depends(get_session())) -> WorkoutsSchema:
        db.delete(WorkoutsModel).where(WorkoutsModel.id == workouts_id)
        db.commit()
        db.refresh()
        db.close()
        return "workout with {workouts_id} is deleted"
