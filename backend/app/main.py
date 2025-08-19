from fastapi import APIRouter, FastAPI
from backend.app.db.database import create_db_and_tables
from backend.app.routers.nutritions import router as nutrition_router
from backend.app.routers.progress import router as progress_router
from backend.app.routers.users import router as users_router
from backend.app.routers.workouts import router as workouts_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def home():
    return ("Hi working fine here")

app.include_router(nutrition_router, prefix="/nutrition");
app.include_router(users_router, prefix="/users");
app.include_router(progress_router, prefix="/progress");
app.include_router(workouts_router, prefix="/workouts");
