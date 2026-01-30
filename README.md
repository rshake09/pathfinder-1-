# pathfinder-1-

CodeCollab Project: A web-based chatbot designed to help students explore academic majors, career paths, and universities based on their interests, GPA, strengths, and goals

# packages

Create a virtual environment
python3 -m venv .venv

Activate
source .venv/bin/activate

pip install google-genai uvicorn fastapi
pip install python-dotenv

# How to run

Run this in one terminal:
streamlit run app.py

Run this in a separate terminal(FastAPI server)
uvicorn main:app --reload

# How to get api key

Verify your age for your personal google account, must be 18+
Show driver license through here:https://myaccount.google.com/age-verification?p=2&avl=1&utm_source=p2
Go here and create key: https://aistudio.google.com/
Create a .env file
Inside file insert: GEMINI_API_KEY = “Your key here”
