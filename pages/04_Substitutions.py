"""Substitutions page for the 5/3/1 Fitness Tracker."""

import streamlit as st
from utils.shared_functions import get_sample_substitutions


def substitutions_page():
    """Exercise substitution page."""
    st.header("🔄 Exercise Substitutions")

    if not st.session_state.program_generated:
        st.warning("⚠️ Please complete setup first!")
        return

    st.subheader("Request Exercise Substitutions")

    col1, col2 = st.columns(2)

    with col1:
        exercise_to_replace = st.text_input(
            "Exercise to replace", placeholder="e.g., Barbell Squat"
        )

        muscle_group = st.selectbox(
            "Muscle group", ["Chest", "Back", "Legs", "Shoulders", "Arms", "Core"]
        )

    with col2:
        st.markdown("**Substitution Options:**")
        if st.button("🔍 Get Substitutions", use_container_width=True):
            if exercise_to_replace:
                substitutions = get_sample_substitutions(
                    exercise_to_replace, muscle_group
                )
                st.json(substitutions)
            else:
                st.error("Please enter an exercise to replace.")


# Page content runs automatically
substitutions_page()
