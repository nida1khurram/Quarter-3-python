import streamlit as st

st.title("User info app")
name = st.text_input("what is your name?")
# age = st.slider("what is your age?",0,100)
age = st.number_input("Enter your age :", value=0)
fav_no = st.text_input("what is your favourit No?")
if st.button("Submit!"):
    st.write(f"Hello :{name}! you are {age} years old, and your favourit No is {fav_no}.")