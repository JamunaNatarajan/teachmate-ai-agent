import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st

# Import all tab modules
from app.ui import class_log_tab
from app.ui import marks_analyzer_tab
from app.ui import login   # 👈 This loads the login UI
from app.ui import (
    syllabus_generator,
    lesson_plan_creator,
    assessment_builder,
    resource_recommender,
    feedback_tracker,
    ai_copilot,
    rag_uploader,
    rag_qa,
    attendance_report_tab,

)

# Page configuration
st.set_page_config(
    page_title="TeachMate AI Agent",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar header
st.sidebar.title("📘 TeachMate AI Agent")
st.sidebar.markdown("Empowering educators with AI-powered productivity tools.")

# All available tabs
TABS = {
    "Syllabus Generator": syllabus_generator.render,
    "Lesson Plan Creator": lesson_plan_creator.render,
    "Assessment Builder": assessment_builder.render,
    "Resource Recommender": resource_recommender.render,
    "Feedback Tracker": feedback_tracker.render,
    "Chat with AI Co-Pilot": ai_copilot.render,
    "RAG Document Uploader": rag_uploader.render,
    "RAG-Powered Q&A": rag_qa.render,
    "Attendance Report Generator": attendance_report_tab.render,
    "Marks Analyzer": marks_analyzer_tab.render,
    "Class Log Entry": class_log_tab.render,

}
# 🔐 LOGIN CHECK
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login.render()
    st.stop()

# Sidebar navigation
selected_tab = st.sidebar.radio("🧭 Choose a Module", list(TABS.keys()))
st.sidebar.markdown(f"👋 Welcome, **{st.session_state.username}**")
if st.sidebar.button("🔓 Logout"):
    st.session_state.logged_in = False
    st.rerun()

# Header title
st.title("📚 TeachMate AI Agent – Smart Assistant for Educators")

# Render selected tab
TABS[selected_tab]()