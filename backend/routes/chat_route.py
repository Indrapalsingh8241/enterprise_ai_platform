from fastapi import APIRouter
from backend.services.chat_services import ask_question

router = APIRouter()

@router.post("/chat")
def chat(question: str):
    

    answer = ask_question(question)

    return {
        "answer": answer
    }