import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel

import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_syllabus(course_name: str, objectives: str, duration_weeks: int = 15) -> str:
    prompt = f"""You are an AI-powered academic planner.

Create a structured {duration_weeks}-week syllabus for a course titled "{course_name}".

Course objectives:
{objectives}

Each week should include:
- Main topic(s)
- Suggested subtopics
- Activity (e.g., case study, quiz, lab)

Use simple bullet points."""
    response = model.generate_content(prompt)
    return response.text
