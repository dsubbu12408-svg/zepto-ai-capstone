from fastapi import FastAPI
from pydantic import BaseModel
from support_assistant.rag import retrieve_policy
app = FastAPI(title="Zepto Support Assistant")


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Zepto Support Assistant API is running"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    documents = retrieve_policy(request.question)

    return {
        "answer": documents[0] if documents else "No relevant policy found.",
        "sources": documents,
        "confidence": 1.0
    }