import streamlit as st
from app.agents import pdf_qa_agent

def render():
    st.header("📄 PDF Q&A Bot")

    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    question = st.text_input("Ask a question about the uploaded PDF")

    if uploaded_file and question:
        with st.spinner("Extracting and generating..."):
            text = pdf_qa_agent.extract_text_from_pdf(uploaded_file)
            if "Error" in text:
                st.error(text)
            else:
                answer = pdf_qa_agent.ask_question_about_pdf(text, question)
                st.success("Answer:")
                st.write(answer)
