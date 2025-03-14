#streamlit app
import streamlit as st
import json  # to save data on local database

# Load & save data
def load_library():
    try:
        # Open json file r --> read
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Initialize library
library = load_library()

# Save data
def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Streamlit interface
st.markdown(
    """
    <h1 style='color: blue;'>Welcome to My Personal Library!</h1>
    <p><strong>"Education is the passport to the future, and the library is the gateway to that passport."</strong> –<em> Malcolm X</em>.</p>
    """,
    unsafe_allow_html=True  # Allow HTML rendering
)
# Sidebar menu with emojis
st.sidebar.title(" 👇 Plz Select an option")
menu = st.sidebar.radio("Your Library", ["📖 View Library", "➕ Add Book", "❌ Remove Book", "🔍 Search Book", "💾 Save & Exit"])

if menu == "📖 View Library":
    st.subheader("📚 Your Library")
    if library:
        st.table(library)
    else:
        st.write("Your Library is empty. Please add books! 📖")

# Add book
elif menu == "➕ Add Book":
    st.subheader("➕ Add a new Book")
    title = st.text_input("📝 Title")
    author = st.text_input("🖋️ Author")
    year = st.number_input("📅 Year", min_value=1800, max_value=2023, step=1)
    genre = st.text_input("📚 Genre")
    read_status = st.checkbox("✅ Mark as Read")
    if st.button("➕ Add Book"):
        # Append last added book in data
        library.append({"title": title, "author": author, "year": int(year), "genre": genre, "read_status": read_status})
        save_library()
        st.success("✅ Book added Successfully!")

# Remove Book
elif menu == "❌ Remove Book":
    st.subheader("❌ Remove a book")
    # For loop to search book titles
    book_titles = [book["title"] for book in library]
    if book_titles:
        selected_book = st.selectbox("Select a book to remove", book_titles)
        if st.button("❌ Remove Book"):
            # Create a new list excluding the selected book
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("✅ Book removed successfully!")
    else:
        st.warning("No book in library. Please add some books! 📖")

# Search book
elif menu == "🔍 Search Book":
    st.subheader("🔍 Search a Book")
    search_term = st.text_input("Enter Title or Author name")
    if st.button("🔍 Search"):
        results = [book for book in library if
                   search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No book found! 🔍")

# Save & exit
elif menu == "💾 Save & Exit":
    save_library()
    st.success("💾 Library saved successfully!")

st.sidebar.subheader("Created by Nida Khurram")
st.sidebar.markdown("Connect with me on :🔗 [LinkedIn](https://www.linkedin.com/in/nida-khurram/)")
# Set full-page background color using custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #99afc2;  /* Light blue background color for the entire page */
    }
    .stSidebar {
        background-color: #f0f2f6;  /* Light gray background color for the sidebar */
    }
    .stButton button {
        background-color: #76a0c4;  /* Green button color */
        color: white;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #537491;  /* Darker green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True # Allow HTML rendering
)