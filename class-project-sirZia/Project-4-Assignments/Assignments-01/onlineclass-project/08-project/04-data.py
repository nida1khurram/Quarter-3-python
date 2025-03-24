import streamlit as st
import pandas as pd
# ____________1_________________
# this data is downloadable
#dictonery
# all array equal
# st.title("Data in Table form")
# data = {"Name":["nida","khurram","arshman","irha"],
#         "Age":[39,50,6,3],
#         "City":["Karachi","Islamabad","Lahore","Multan"]}

# df = pd.DataFrame(data)

# # st.dataframe(df) #scrollable
# st.table(df) #non scrollable

# _______________2__________________________
# data = {"Name":["nida","khurram","arshman","irha"],
#         "Age":[39,50,6,3],
#         "City":["Karachi","Islamabad","Lahore","Multan"]}

# df = pd.DataFrame(data)
# st.title("Choose Data")
# choose_city = st.selectbox("Choose city to filter",df["City"].unique())
# filtered_data = df[df["City"] == choose_city]
# st.write(f"Data for city: {choose_city}")
# st.dataframe(filtered_data)

# _______________3_________________________
# data = {"Name":["nida","khurram","arshman","irha"],
#         "Age":[39,50,6,3],
#         "City":["Karachi","Islamabad","Lahore","Multan"],
#         "score":[88,70,49,95]}

# df = pd.DataFrame(data)
# st.title("Data with style")
# def data_style(val):
#     if isinstance(val, int) and val > 90:
#         return 'background-color: yellow'
#     return ''

# # Apply the function to the DataFrame
# styled_df = df.style.apply(lambda x: x.map(data_style))

# st.dataframe(styled_df)
# ________________ 4 ___________________
data = {"Name":["nida","khurram","arshman","irha"],
        "Age":[39,50,6,3],
        "City":["Karachi","Islamabad","Lahore","Multan"],
        "score":[28,70,39,95]}

df = pd.DataFrame(data)
st.title("Data with style & user input")
"""
Get an user input as number input and filter based on that number defaulty its going to be 80
"""
# User input for the minimum value to highlight
value_of_style = st.number_input("Enter the minimum number to display in yellow", value=40)

# Function to apply styling based on the user input
def highlight_values(val, threshold):
    if isinstance(val, int) and val >= threshold:
        return "background-color: yellow"
    return ""

# Apply the styling function to the DataFrame
styled_df = df.style.apply(lambda x: x.map(lambda val: highlight_values(val, value_of_style)))

# Display the styled DataFrame
st.dataframe(styled_df)