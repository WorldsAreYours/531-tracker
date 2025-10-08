"""Home page for the 5/3/1 Fitness Tracker."""

import streamlit as st


def home_page():
    """Welcome page with overview and instructions."""
    st.header("Welcome to Your 5/3/1 Fitness Tracker!")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
        ### What is 5/3/1?
        The 5/3/1 program is a strength training method created by Jim Wendler. 
        It focuses on four main lifts:
        - **Squat**
        - **Bench Press** 
        - **Deadlift**
        - **Overhead Press**
        
        ### How it Works
        1. **Calculate Training Max**: 90% of your 1RM
        2. **4-Week Cycles**: Each week uses different percentages
        3. **Progressive Overload**: Increase weights each cycle
        4. **Accessory Work**: Additional exercises for muscle development
        
        ### Getting Started
        Use the **Setup** page to enter your 1RM estimates and preferences.
        """
        )

    with col2:
        st.info(
            """
        **Quick Start:**
        1. Go to Setup page
        2. Enter your 1RM estimates
        3. Choose workout frequency
        4. Generate your program!
        """
        )

    # Show current status
    if st.session_state.program_generated:
        st.success("✅ Program generated! Check out the Program page.")
    else:
        st.warning("⚠️ No program generated yet. Start with the Setup page.")


# Page content runs automatically
home_page()
