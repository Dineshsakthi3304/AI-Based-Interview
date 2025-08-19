from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for local frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    history: list

INTERVIEW_QUESTIONS = [
    "Tell me about yourself.",
    "Why do you want to work at our company?",
    "What are your strengths and weaknesses?",
    "Describe a challenge you faced and how you overcame it.",
    "Where do you see yourself in five years?",
]

@app.post("/chat")
async def chat(request: ChatRequest):
    history = request.history or []
    idx = len(history)

    # If there was an answer from user, record it with the last question
    if idx > 0:
        last_question = INTERVIEW_QUESTIONS[idx-1] if idx-1 < len(INTERVIEW_QUESTIONS) else "Last Question"
        # Avoid double-adding answers if already present
        if len(history) < idx or (len(history) == idx and history[-1].get("answer") != request.message):
            history.append({"question": last_question, "answer": request.message})

    if idx < len(INTERVIEW_QUESTIONS):
        reply = INTERVIEW_QUESTIONS[idx]
    else:
        # Interview finished: summarize answers
        summary = ["Interview complete! Here's a summary of your answers:"]
        for item in history:
            question = item.get("question", "Question")
            answer = item.get("answer", "No answer given")
            summary.append(f"{question}\nYour answer: {answer}")
        reply = "\n\n".join(summary)

    return {"reply": reply}
