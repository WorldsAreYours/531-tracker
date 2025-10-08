"""Setup page for the 5/3/1 Fitness Tracker."""

import streamlit as st
from utils.shared_functions import generate_sample_program


def setup_page():
    """Setup page for user input and program generation."""
    st.header("⚙️ Program Setup")

    with st.form("setup_form"):
        st.subheader("Main Lifts - 1RM Estimates")

        col1, col2 = st.columns(2)
        with col1:
            squat_1rm = st.number_input(
                "Squat 1RM (lbs)",
                min_value=0,
                value=225,
                help="Your estimated 1-rep max for squats",
            )
            bench_1rm = st.number_input(
                "Bench Press 1RM (lbs)",
                min_value=0,
                value=185,
                help="Your estimated 1-rep max for bench press",
            )

        with col2:
            deadlift_1rm = st.number_input(
                "Deadlift 1RM (lbs)",
                min_value=0,
                value=275,
                help="Your estimated 1-rep max for deadlifts",
            )
            ohp_1rm = st.number_input(
                "Overhead Press 1RM (lbs)",
                min_value=0,
                value=135,
                help="Your estimated 1-rep max for overhead press",
            )

        st.subheader("Workout Preferences")
        workouts_per_week = st.selectbox(
            "Workouts per week",
            [3, 4, 5, 6],
            index=1,
            help="How many days per week do you want to train?",
        )

        workout_duration = st.slider(
            "Workout duration (minutes)",
            30,
            120,
            60,
            help="How long do you want each workout to be?",
        )

        submitted = st.form_submit_button(
            "🚀 Generate Program", use_container_width=True
        )

        if submitted:
            # Store user data
            st.session_state.user_data = {
                "squat_1rm": squat_1rm,
                "bench_1rm": bench_1rm,
                "deadlift_1rm": deadlift_1rm,
                "ohp_1rm": ohp_1rm,
                "workouts_per_week": workouts_per_week,
                "workout_duration": workout_duration,
            }

            # Generate program (placeholder for now)
            st.session_state.program = generate_sample_program(
                st.session_state.user_data
            )
            st.session_state.program_generated = True

            st.success("🎉 Program generated successfully!")
            st.balloons()


# Page content runs automatically
setup_page()
