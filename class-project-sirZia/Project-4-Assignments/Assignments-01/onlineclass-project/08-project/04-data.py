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
