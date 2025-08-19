from fastapi import APIRouter, Depends
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import session
from backend.app.db.database import get_session
from backend.app.models.Nutritions import NutritionsModel
from backend.app.schemas.Nutritions import NutritionsSchema

router = APIRouter();

@router.get("/") 
def get_all_nutrition(db: session = Depends(get_session())) -> list[NutritionsSchema]:
    return db.scalars(select(NutritionsModel))

@router.get("/{nutritions_id}") 
def get_nutrition(nutritions_id, db: session = Depends(get_session())) -> NutritionsSchema:
    return db.scalars(select(NutritionsModel).where(NutritionsModel.id == nutritions_id)).one()

@router.post("/") 
def add_nutrition(postNutrition : NutritionsSchema, db: session = Depends(get_session())) -> NutritionsSchema:
    db.add(postNutrition);
    db.commit()
    obj = db.refresh()
    db.close()
    return obj

@router.put("/{nutritions_id}") 
def add_nutrition(postNutrition : NutritionsSchema, nutritions_id, db: session = Depends(get_session())) -> NutritionsSchema:
        return db.insert(NutritionsModel).where(NutritionsModel.id == nutritions_id).values(NutritionsModel.meals==postNutrition.meals, 
            NutritionsModel.macros==postNutrition.macros)

@router.delete("/{nutritions_id}") 
def delete_nutrition(nutritions_id, db: session = Depends(get_session())) -> NutritionsSchema:
        return db.delete(NutritionsModel).where(NutritionsModel.id == nutritions_id)
