from fastapi import APIRouter, Depends
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import session
from backend.app.db.database import get_session
from backend.app.models.Progress import ProgressModel
from backend.app.schemas.Progress import ProgressSchema

router = APIRouter();

@router.get("/") 
def get_all_progress(db: session = Depends(get_session())) -> list[ProgressSchema]:
    return db.scalars(select(ProgressModel))

@router.get("/{progress_id}") 
def get_progress(progress_id, db: session = Depends(get_session())) -> ProgressSchema:
    return db.scalars(select(ProgressModel).where(ProgressModel.id == progress_id)).one()

@router.post("/") 
def add_progress(postProgress : ProgressSchema, db: session = Depends(get_session())) -> ProgressSchema:
    db.add(postProgress);
    db.commit()
    obj = db.refresh()
    db.close()
    return obj

@router.put("/{progress_id}") 
def add_progress(postProgress : ProgressSchema, progress_id, db: session = Depends(get_session())) -> ProgressSchema:
        db.insert(ProgressModel).where(ProgressModel.id == progress_id).values(ProgressModel.sets==postProgress.sets, 
            ProgressModel.reps==postProgress.reps, ProgressModel.weight==postProgress.weight, ProgressModel.notes==postProgress.notes)
        db.commit()
        db.refresh()
        db.close()
        return postProgress

@router.delete("/{progress_id}") 
def delete_progress(progress_id, db: session = Depends(get_session())) -> ProgressSchema:
        db.delete(ProgressModel).where(ProgressModel.id == progress_id)
        db.commit()
        db.refresh()
        db.close()
        return "progress with {progress_id} is deleted"
