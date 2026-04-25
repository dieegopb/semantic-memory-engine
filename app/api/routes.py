from fastapi import APIRouter
from pydantic import BaseModel
from app.services.qa_service import QAService

router = APIRouter()

# ✅ DEFINE O SCHEMA
class QuestionRequest(BaseModel):
    user_id: str
    question: str

@router.post("/ask")
def ask(request: QuestionRequest):
    service = QAService()
    return service.ask(request.user_id, request.question)