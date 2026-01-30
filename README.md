# pathfinder-1-

CodeCollab Project: A web-based chatbot designed to help students explore academic majors, career paths, and universities based on their interests, GPA, strengths, and goals

# packages

## Create a virtual environment
python3 -m venv .venv

## Activate enviroment
source .venv/bin/activate

## To leave venv
ctrl+c

## Install packages
pip install google-genai uvicorn fastapi streamlit<br>
pip install python-dotenv

# How to run

## Run this in one terminal:
streamlit run app.py

## Run this in a separate terminal(FastAPI server)
uvicorn main:app --reload

# How to get api key

1.Verify your age for your personal google account, must be 18+
2.Show driver license through here:https://myaccount.google.com/age-verification?p=2&avl=1&utm_source=p2
3.Go here and create key: https://aistudio.google.com/
4.Create a .env file
5.Inside file insert: GEMINI_API_KEY = “Your key here”
