import streamlit as st
# st.title("Column")
# col1, col2 = st.columns(2)
# with col1:
#     st.header("Column 1")
#     st.write("This is the first column")
#     st.button("Button 1")

# with col2:
#     st.header("Column 2")
#     st.write("This is the second column")
#     st.button("Button 2")
# ________________2_______________
# st.title("Expender")
# with st.expander("See more details"):
#     st.write("Here are some additional details that can be toggled.")
#     st.line_chart([1,2,3,4,5])
# ________________ 3 pages____________
# st.sidebar.title("Navigation")
# option = st.sidebar.selectbox("Choose a page: ",["Home","About","Contact"])
# if option == "Home":
#     st.write("Welcome to the Home page!")
# elif option == "About":
#     st.write("This is About page!")
# elif option == "Contact":
#     st.write("This is Contact page!")
# _______________4 page layout____________________
st.set_page_config(page_title="Themed App", layout="wide", initial_sidebar_state="expanded")
st.title("Themed Streamlit App")
st.write("This app has a customized theme!") 