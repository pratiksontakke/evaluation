from fastapi import APIRouter

router = APIRouter();

@router.get("/")
def get_nutrition():
    return "inside nutrition router"

