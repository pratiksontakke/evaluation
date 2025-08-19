from fastapi import APIRouter
from backend.app.schemas.Chat import ChatRequest, ChatResponse
from backend.app.services.rag_google_chain import get_rag_chain

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def handle_chat(request: ChatRequest):
    chain = get_rag_chain()
    answer = chain.invoke(request.question)
    return ChatResponse(answer=answer)