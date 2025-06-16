import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_feedback_suggestions(course_name: str, what_worked: str, what_did_not: str) -> str:
    prompt = f"""You are an AI academic mentor.

Based on the weekly teaching feedback for the course "{course_name}", suggest actionable improvements.

✅ What worked: {what_worked}

❌ What didn’t work: {what_did_not}

Respond with 2–3 suggestions for improvement in a clear and helpful tone."""
    response = model.generate_content(prompt)
    return response.text
