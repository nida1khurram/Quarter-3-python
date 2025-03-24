import streamlit as st
st.logo("flower.jpg", size="large", link=None, icon_image=None)

st.title("This is my Streamlit app!")
st.image("flower.jpg", caption="This is a beautiful flower")

st.header("This is header")
st.subheader("This is subheader")
st.text("This is text")
st.markdown("**This is bold text using markdown**")

name = "Nida Khurram"
number = 7
st.write(f"Hello, {name}. Here's a number: {number}")

if st.button("Click Me!"):
    st.write("Hi")
#checkbox  true or false
checked = st.checkbox("Check Me!")
if checked:
    st.write("Checkbox is check!")
# slider
age = st.slider("Select your age",0,100,40)
st.write("Your age is :", age)
#input
name = st.text_input("Enter your name", value= "")
st.write("Hello, ", name)


