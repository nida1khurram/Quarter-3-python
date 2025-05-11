# Import the Streamlit library
import streamlit as st

# Hide the GitHub link in the top right corner
hide_github_link = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_github_link, unsafe_allow_html=True)

# Set the title of the app
st.title("Simple Quiz App")

# Define the quiz questions, correct answers, and multiple-choice options
quiz_questions = {
    "What is the use of the 'print' function in Python?": {
        "options": ["To take user input", "To display output", "To perform calculations", "To define a function"],
        "correct_answer": "To display output"
    },
    "Why is Streamlit used?": {
        "options": ["For game development", "For creating web apps", "For machine learning models", "For database management"],
        "correct_answer": "For creating web apps"
    },
    "What is the difference between a list and a tuple in Python?": {
        "options": ["List is immutable, tuple is mutable", "List is mutable, tuple is immutable", "Both are mutable", "Both are immutable"],
        "correct_answer": "List is mutable, tuple is immutable"
    },
    "What is the use of the Pandas library?": {
        "options": ["For web development", "For data analysis and manipulation", "For creating games", "For machine learning"],
        "correct_answer": "For data analysis and manipulation"
    }
}

# Initialize a variable to track the user's score
score = 0

# Loop through each question and display it
for question, data in quiz_questions.items():
    st.write(f"**Question:** {question}")
    
    # Display multiple-choice options using a radio button
    user_answer = st.radio(
        f"Select the correct answer for: {question}",
        options=data["options"],
        key=question
    )
    
    # Check if the user has selected an answer
    if user_answer:
        # Compare the user's answer with the correct answer
        if user_answer == data["correct_answer"]:
            st.success("Correct! 🎉")
            score += 1  # Increment the score
        else:
            st.error(f"Wrong! 😢 The correct answer is: {data['correct_answer']}")

# Display the final score after the quiz is completed
st.write("---")
st.write(f"### Your final score is: {score}/{len(quiz_questions)}")

# If the user answered all questions correctly, show a celebration message
if score == len(quiz_questions):
    st.balloons()  # Celebration animation
    st.success("Congratulations! You aced the quiz! 🎉🎉")