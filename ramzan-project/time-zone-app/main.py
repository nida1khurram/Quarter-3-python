# Import required libraries
import streamlit as st
# datetime ki class se import kia datetime k module ko 
from datetime import datetime
#world time info import 
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]
st.title("Time Zone App")
# Create a multi-select dropdown for choosing time zones
selected_timezone = st.multiselect("Select Time Zone", TIME_ZONES, default=["UTC","Asia/Karachi"])
st.subheader("Selected Timezone")
for tz in selected_timezone:
     #class         class    str formate func Y->year m->month d->day i->currenttime
    # current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H %M %S %P")#H->hr M->min S->sec %P-> 12 formate convert
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
     # Display timezone and its current time
    st.write(f"**{tz}**: {current_time}")



# Create section for time conversion
st.subheader("Convert Time Between Timezones")
# Create time input field with current time as default
current_time = st.time_input("Current Time", value=datetime.now().time())
# Dropdown to select source timezone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
# Dropdown to select target timezone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Create convert button and handle conversion
if st.button("Convert Time"):
    # Combine today's date with input time and source timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    # Convert time to target timezone and format it with AM/PM
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display the converted time with success message
    st.success(f"Converted Time in {to_tz}: {converted_time}")