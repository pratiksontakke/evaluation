from fastapi import APIRouter, Depends
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import session
from backend.app.db.database import get_session
from backend.app.models.Users import UsersModel
from backend.app.schemas.Users import UsersSchema

router = APIRouter();

@router.get("/") 
def get_all_users(db: session = Depends(get_session())) -> list[UsersSchema]:
    return db.scalars(select(UsersModel))

@router.get("/{users_id}") 
def get_user(users_id, db: session = Depends(get_session())) -> UsersSchema:
    return db.scalars(select(UsersModel).where(UsersModel.id == users_id)).one()

@router.post("/") 
def add_user(postUser : UsersSchema, db: session = Depends(get_session())) -> UsersSchema:
    db.add(postUser);
    db.commit()
    obj = db.refresh()
    db.close()
    return obj

@router.put("/{users_id}") 
def add_user(postUser : UsersSchema, users_id, db: session = Depends(get_session())) -> UsersSchema:
        db.insert(UsersModel).where(UsersModel.id == users_id).values(UsersModel.password==postUser.password, 
            UsersModel.age==postUser.age, UsersModel.weight==postUser.weight, UsersModel.height==postUser.height, UsersModel.goals==postUser.goals)
        db.commit()
        db.refresh()
        db.close()
        return postUser

@router.delete("/{users_id}") 
def delete_user(users_id, db: session = Depends(get_session())) -> UsersSchema:
        db.delete(UsersModel).where(UsersModel.id == users_id)
        db.commit()
        db.refresh()
        db.close()
        return "user with {users_id} is deleted"
