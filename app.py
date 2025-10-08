"""Main application entry point for the 5/3/1 Fitness Tracker."""

import streamlit as st

st.set_page_config(
    page_title="5/3/1 Fitness Tracker",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
if "program_generated" not in st.session_state:
    st.session_state.program_generated = False
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
if "program" not in st.session_state:
    st.session_state.program = None

st.title("💪 5/3/1 Fitness Tracker")
st.markdown("---")

st.write(
    """
    Welcome to your 5/3/1 Fitness Tracker! 
    
    Use the sidebar navigation to:
    - **Setup**: Enter your 1RM estimates and preferences
    - **Program**: View your generated 4-week program
    - **Substitutions**: Get alternative exercises
    
    Navigate using the sidebar to get started!
    """
)

# Show current status
if st.session_state.program_generated:
    st.success("✅ Program generated! Check out the Program page in the sidebar.")
else:
    st.warning("⚠️ No program generated yet. Start with the Setup page in the sidebar.")
