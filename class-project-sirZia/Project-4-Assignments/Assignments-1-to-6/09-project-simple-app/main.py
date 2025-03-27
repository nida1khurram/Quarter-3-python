import streamlit as st
# st.title("Welcome To Simple App")
# st.write("Hello World")
# st.write({"key":["value"]})

# _____________ 2
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")
uploaded_file = st.file_uploader("Choose a csv file", type="csv")
if uploaded_file is not None:
    # st.write("File Uploaded...")
    df = pd.read_csv(uploaded_file)
# ________________________________________
    st.subheader("Data Preview")
    st.write(df.head())
# ____________________________________
    st.subheader("Data Summary")
    st.write(df.describe())
# ________________________________________
    st.write("Filter Data")
    columns = df.columns.to_list()
    selected_column = st.selectbox("Select column to filter by ",columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select Value",unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
# __________________________________________________
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column",columns)
    y_column = st.selectbox("Select y-axis column",columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
        
else:
    st.write("Waiting on file upload...")
