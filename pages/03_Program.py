"""Program page for the 5/3/1 Fitness Tracker."""

import streamlit as st
from utils.shared_functions import get_week_description, display_week_program


def program_page():
    """Display the generated 5/3/1 program."""
    st.header("📋 Your 5/3/1 Program")

    if not st.session_state.program_generated:
        st.warning("⚠️ Please complete setup first!")
        st.info("Go to the Setup page to generate your program.")
        return

    # Display user data summary
    st.subheader("Your Settings")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Workouts/Week", st.session_state.user_data["workouts_per_week"])
    with col2:
        st.metric("Duration", f"{st.session_state.user_data['workout_duration']} min")
    with col3:
        st.metric("Training Maxes", "Calculated")

    # Display 4-week program
    st.subheader("4-Week Program")

    for week in range(1, 5):
        with st.expander(f"Week {week} - {get_week_description(week)}"):
            display_week_program(week)


# Page content runs automatically
program_page()
