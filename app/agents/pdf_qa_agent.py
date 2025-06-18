import fitz  # PyMuPDF
import google.generativeai as genai
import os

# Load Gemini API Key
genai.configure(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(pdf_file):
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def ask_question_about_pdf(text, question):
    limited_text = text[:6000]  # Limit to avoid token overflow
    prompt = f"""
You are a helpful assistant. The user uploaded a PDF and asked a question.

PDF Content:
{limited_text}

Question:
{question}

Answer:
"""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during generation: {str(e)}"
