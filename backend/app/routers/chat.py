from fastapi import APIRouter, Depends
from backend.app.schemas.Chat import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def handle_chat(request: ChatRequest):
    return ChatResponse()