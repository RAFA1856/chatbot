from fastapi import APIRouter
from pydantic import BaseModel
from chatbot import get_response

router = APIRouter()

class UserInput(BaseModel):
    message: str

@router.post("/chat")
async def chat(user_input: UserInput):
    return get_response(user_input.message)