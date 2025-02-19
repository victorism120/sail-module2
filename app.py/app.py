import streamlit as st
import pandas as pd


# Set page config
st.set_page_config(
    page_title="Student Scores Manager",
    page_icon="📚",
    layout="wide"

# Initialize session state for student data
if "students" not in st.session_state:
    st.session_state.students = []

def add_student(name, score):
    """Add a student and their score to the session state."""
    if name and score is not None:  # Ensure both fields are filled
        st.session_state.students.append({"name": name, "score": score})
        return True
    return False

# Task 1: Input and display student data
st.header("Student Data Input")

col1, col2 = st.columns(2)  # Arrange input fields side by side

with col1:
    student_name = st.text_input("Student Name")
with col2:
    student_score = st.number_input("Student Score", min_value=0, step=1)  # Ensure non-negative scores

if st.button("Add Student"):
    if student_name and student_score is not None:  # Check if both inputs are provided
        st.session_state.students.append({"name": student_name, "score": student_score})
        st.success(f"Student '{student_name}' added successfully!")  # User feedback
    else:
        st.warning("Please enter both name and score.")  # User feedback

if st.session_state.students:
    df_students = pd.DataFrame(st.session_state.students)  # Create a DataFrame
    st.subheader("Student Data Table")
    st.dataframe(df_students)  # Display the DataFrame

# Task 2: Filter by minimum score
st.header("Student Data Filter")

min_score = st.slider("Minimum Score", min_value=0, max_value=100, value=0)  # Slider for filtering

if st.session_state.students:
    filtered_students = df_students[df_students["score"] >= min_score]  # Filter the DataFrame
    st.subheader(f"Students with Score >= {min_score}")
    if not filtered_students.empty:
        st.dataframe(filtered_students)  # Display the filtered DataFrame
    else:
        st.info("No students meet the minimum score criteria.") # User feedback
