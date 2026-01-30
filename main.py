from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from aiservice import AIService


load_dotenv()

app=FastAPI(title="AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai_service = AIService()

users = {} #user profile storage

messages = {} #message storage

class AskRequest(BaseModel):
    user_id: str
    message: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

#Creates a user profile 
@app.post("/ask")
def ask(request: AskRequest):
    print(f"Received request: user_id={request.user_id}, message={request.message}")
    user_id = request.user_id
    message = request.message

    #initializes profile if they are not in data set
    if user_id not in users:
        users[user_id] = {"gpa": None, "interests": [], "strengths": [], "goals": []}

    if user_id not in messages:
        messages[user_id] = []

    #appends messages to keep a history of chat
    messages[user_id].append({"role": "user", "content": message})

    #gets current user and their information
    user_profile = users[user_id]
    context = f"""
    User Profile:
    - GPA: {user_profile['gpa']}
    - Interests: {', '.join(user_profile['interests'])}
    - Strengths: {', '.join(user_profile['strengths'])}
    - Goals: {', '.join(user_profile['goals'])}
    
    Conversation history:
    {messages[user_id]}
    """

    #create response
    response = ai_service.chat(message, context)

    #we use the the term assistant to make history of chat cleaner
    messages[user_id].append({"role": "assistant", "content": response})

    return {"response": response}

@app.get("/messages/{user_id}")
def get_messages(user_id: str):
    if user_id not in messages:
        return {"messages": []}
    
    return {"messages": messages[user_id]}