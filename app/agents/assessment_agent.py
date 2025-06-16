import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel

import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_assessment(course_name: str, unit_name: str, num_questions: int, question_type: str, bloom_level: str) -> str:
    prompt = f"""Generate {num_questions} {question_type} questions for the course "{course_name}", unit "{unit_name}".
Follow Bloom's taxonomy level: {bloom_level}.
Include variety. Keep aligned with undergraduate curriculum.
Use clean numbered format and provide options for MCQs if needed."""
    response = model.generate_content(prompt)
    return response.text
