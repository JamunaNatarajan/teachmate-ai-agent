import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel

import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_copilot_response(query: str) -> str:
    prompt = f"""You are an AI teaching co-pilot. Help educators with classroom activities, teaching suggestions, concept explanations, and planning support.

Here is the educator’s query:
{query}

Respond clearly and helpfully."""
    response = model.generate_content(prompt)
    return response.text
