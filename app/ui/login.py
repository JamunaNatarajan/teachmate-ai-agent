import streamlit as st

def render():
    st.title("🔐 Login to TeachMate")

    # Pre-defined usernames and passwords
    valid_users = {
        "varun": "1234",      # you can change these
        "prof1": "abcd"
    }

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in valid_users and password == valid_users[username]:
            st.success("✅ Login successful!")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("❌ Invalid username or password")
