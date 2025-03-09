import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 100)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = generate_money()
    st.balloons()  # Celebration animation
    st.success(f"Congratulations! You made ${amount}!🎉🎉")
#side hustle func
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return("Freelancing")
    except:
        return("Something went wrong!")
#ui hustles
st.subheader("Side hustle ideas")
if st.button("Generate hustles"):
    idea = fetch_side_hustle()
    st.success(idea)

#money quotes func
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return("Money is the root of all evil!")
    except:
        return("Something went wrong!")
#ui quotes
st.subheader("Money Making Motivation")
if st.button("Money Quotes"):
    money_idea = fetch_money_quote()
    st.info(money_idea)
        

