"""Shared utility functions used across pages."""

import streamlit as st


def get_week_description(week):
    """Get description for each week."""
    descriptions = {
        1: "Base Week (65/75/85%)",
        2: "Build Week (70/80/90%)",
        3: "Peak Week (75/85/95%)",
        4: "Deload Week (40/50/60%)",
    }
    return descriptions.get(week, "Unknown Week")


def display_week_program(week):
    """Display the program for a specific week."""
    st.markdown(f"**Week {week} Program:**")

    # Main lifts
    st.markdown("**Main Lifts:**")
    lifts = ["Squat", "Bench Press", "Deadlift", "Overhead Press"]

    for lift in lifts:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.write(f"• {lift}")
        with col2:
            st.write("3 sets")
        with col3:
            st.write("5 reps")

    # Accessory work
    st.markdown("**Accessory Work:**")
    accessories = ["Push-ups", "Pull-ups", "Planks", "Lunges"]

    for accessory in accessories:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.write(f"• {accessory}")
        with col2:
            st.write("3 sets")
        with col3:
            st.write("10-15 reps")


def get_sample_substitutions(exercise, muscle_group):
    """Get sample exercise substitutions."""
    substitutions = {
        "Barbell Squat": ["Goblet Squat", "Bulgarian Split Squat", "Leg Press"],
        "Bench Press": ["Dumbbell Press", "Push-ups", "Incline Press"],
        "Deadlift": ["Romanian Deadlift", "Trap Bar Deadlift", "Kettlebell Swing"],
        "Overhead Press": ["Dumbbell Press", "Pike Push-ups", "Lateral Raises"],
    }

    return {
        "original_exercise": exercise,
        "muscle_group": muscle_group,
        "substitutions": substitutions.get(
            exercise, ["Exercise 1", "Exercise 2", "Exercise 3"]
        ),
        "notes": "These are sample substitutions. Real substitutions will use Groq API.",
    }


def generate_sample_program(user_data):
    """Generate a sample program structure."""
    return {
        "user_data": user_data,
        "weeks": {
            1: {"percentage": "65/75/85", "description": "Base week"},
            2: {"percentage": "70/80/90", "description": "Build week"},
            3: {"percentage": "75/85/95", "description": "Peak week"},
            4: {"percentage": "40/50/60", "description": "Deload week"},
        },
    }
