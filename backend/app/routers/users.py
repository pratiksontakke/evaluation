from fastapi import APIRouter

router = APIRouter();

@router.get("/")
def get_users():
    return "inside users router"

