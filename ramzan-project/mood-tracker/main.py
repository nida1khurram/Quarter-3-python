import streamlit as st
import pandas as pd
import datetime
import csv
import os #to store data read, write on system
 
MOOD_FILE = "mood_log.csv"
# to write data in csv
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        # pd.Dataframe create col in file
        return pd.DataFrame(columns=["Date","Mood"])
    # 
    return pd.read_csv(MOOD_FILE)
# ui parameter ->arguments pass
def save_mood_data(date,mood):
    # a appened r read w write
    with open(MOOD_FILE, "a") as file:
        writer = csv.writer(file)

        writer.writerow([date, mood])

#ui
st.title("Mood Tracker")
today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select you Mood", ["Happy", "Sad", "Angry", "Neutral"])
if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")

# filedata display on ui with help of pandas
# pandas used data manupulation like chart
data = load_mood_data()
if not data.empty:
    