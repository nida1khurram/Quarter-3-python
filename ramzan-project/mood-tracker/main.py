# # 
# import streamlit as st # For creating web interface
# import pandas as pd # For data manipulation
# import datetime # For handling dates
# import csv # For reading and writing CSV file
# import os # For file operations #to store data read, write on system

# # Define the file name for storing mood data
# MOOD_FILE = "mood_log.csv"

# # Function to read mood data from the CSV file # to write data in csv
# def load_mood_data():
#     # Check if the file exists
#     if not os.path.exists(MOOD_FILE):
#         # pd.Dataframe create col in file
#         # If no file, create empty DataFrame with columns
#         return pd.DataFrame(columns=["Date", "Mood"])
#     # Read and return existing mood data
#     return pd.read_csv(MOOD_FILE)

#  # ui parameter ->arguments pass
# # Function to add new mood entry to CSV file
# def save_mood_data(date, mood):
#     # Open file in append mode
#     with open(MOOD_FILE, "a") as file:

#         # Create CSV writer
#         writer = csv.writer(file)

#         # Add new mood entry
#         writer.writerow([date, mood])

# # Streamlit app title
# st.title("Mood Tracker App 😊😢😠😐")

# # Get today's date
# today = datetime.date.today()

# # Create subheader for mood input
# st.subheader("How are your feeling today? ❔")

# # Create dropdown for mood selection
# mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# # Create button to save mood
# if st.button("Log Mood"):
    
#     # Save mood when button is clicked
#     save_mood_data(today, mood)

#     # Show success message
#     st.success("Mood Logged Successfully!")

# # filedata display on ui with help of pandas
# # # pandas used data manupulation like chart
# # Load existing mood data
# data = load_mood_data()

# # If there is data to display
# if not data.empty:

#     # Create section for Visualization
#     st.subheader("Mood Trends Over Time")

#     # Convert date stings to datetime Objects
#     data["Date"] = pd.to_datetime(data["Date"])

#     # Count frequency of each mood
#     mood_counts = data.groupby("Mood").count()["Date"]

#     # Display bar chart of mood frequencies
#     st.bar_chart(mood_counts)

#     # Build with love by Asharib Ali
#     st.write("Build with ❤️ by [Nida Khurram](https://github.com/nida1khurram/Quarter-3-python/tree/main/ramzan-project/mood-tracker)")







import streamlit as st  # For creating web interface
import pandas as pd  # For data manipulation
import datetime  # For handling dates
import csv  # For reading and writing CSV file
import os  # For file operations

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from the CSV file
def load_mood_data():
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If no file, create an empty DataFrame with the correct columns
        df = pd.DataFrame(columns=["Date", "Mood"])
        # Save the empty DataFrame to the CSV file
        df.to_csv(MOOD_FILE, index=False)
        return df
    # Read and return existing mood data
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:
        # Create CSV writer
        writer = csv.writer(file)
        # Add new mood entry
        writer.writerow([date, mood])

# Streamlit app title
st.title("Mood Tracker App 😊😢😠😐")

# Get today's date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How are you feeling today? ❔")

# Create dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mood
if st.button("Log Mood"):
    # Save mood when button is clicked
    save_mood_data(today, mood)
    # Show success message
    st.success("Mood Logged Successfully!")

# Load existing mood data
data = load_mood_data()

# Debugging: Print file path and current working directory
st.write(f"Current working directory: {os.getcwd()}")
st.write(f"File path: {os.path.abspath(MOOD_FILE)}")

# If there is data to display
if not data.empty:
    # Create section for Visualization
    st.subheader("Mood Trends Over Time")
    # Convert date strings to datetime objects
    data["Date"] = pd.to_datetime(data["Date"])
    # Count frequency of each mood
    mood_counts = data.groupby("Mood").count()["Date"]
    # Display bar chart of mood frequencies
    st.bar_chart(mood_counts)
else:
    st.write("No mood data available yet. Log your mood to see trends!")

# Build with love by Asharib Ali
st.write("Build with ❤️ by [Nida Khurram](https://github.com/nida1khurram/Quarter-3-python/tree/main/ramzan-project/mood-tracker)")