from fastapi import FastAPI
from backend.app.db.database import create_db_and_tables
from backend.app.routers.nutritions import router as nutrition_router
from backend.app.routers.progress import router as progress_router
from backend.app.routers.users import router as users_router
from backend.app.routers.workouts import router as workouts_router
from backend.app.routers.chat import router as chat_router
from backend.app.routers.exercises import router as exercises_router
from backend.app.routers.workout_plans import router as workout_plans_router
from backend.app.services.rag_google_chain import initialize_rag_chain

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    initialize_rag_chain()

@app.get("/")
def home():
    return ("Hi working fine here")

app.include_router(nutrition_router, prefix="/nutritions");
app.include_router(users_router, prefix="/users");
app.include_router(progress_router, prefix="/progress");
app.include_router(workouts_router, prefix="/workouts");
app.include_router(chat_router, prefix="/chat");
app.include_router(exercises_router, prefix="/exercises");
app.include_router(workout_plans_router, prefix="/workout-plans");