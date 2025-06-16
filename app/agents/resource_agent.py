import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel

import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_resources(topic: str, difficulty: str, format_types: list) -> str:
    prompt = f"""Act as an academic resource recommender for educators.

Suggest curated online resources to teach the topic: "{topic}".
Student level: {difficulty}
Required formats: {', '.join(format_types)}.

Include relevant blogs, PDFs, videos, case studies, or research papers.
Mention titles with links if possible. Prioritize high-quality and open-access content."""
    response = model.generate_content(prompt)
    return response.text
