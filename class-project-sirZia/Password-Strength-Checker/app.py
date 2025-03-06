import streamlit as st
import re
import random
import string

# Set page title
st.title("🔒 Password Security Tool")

# Create tabs for checker and generator
tab1, tab2 = st.tabs(["Check Password", "Generate Password"])

# Common passwords (shortened list)
COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "welcome", "abc123"]

# Password checker tab
with tab1:
    st.header("Password Strength Checker")
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        # Check if password is common
        if password.lower() in COMMON_PASSWORDS:
            st.error("⚠️ This is a commonly used password!")
        else:
            # Initialize score
            score = 0
            feedback = []
            
            # Length Check
            if len(password) >= 8:
                score += 1
                feedback.append("✅ Good length")
            else:
                feedback.append("❌ Password should be at least 8 characters long")
            
            # Upper & Lowercase Check
            if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
                score += 1
                feedback.append("✅ Good mix of uppercase and lowercase")
            else:
                feedback.append("❌ Include both uppercase and lowercase letters")
            
            # Digit Check
            if re.search(r"\d", password):
                score += 1
                feedback.append("✅ Contains numbers")
            else:
                feedback.append("❌ Add at least one number (0-9)")
            
            # Special Character Check
            if re.search(r"[!@#$%^&*]", password):
                score += 1
                feedback.append("✅ Contains special characters")
            else:
                feedback.append("❌ Include at least one special character (!@#$%^&*)")
            
            # Display progress bar and strength rating
            st.progress(score / 4)
            
            if score == 4:
                st.success("✅ Strong Password!")
            elif score == 3:
                st.warning("⚠️ Moderate Password - Consider adding more security features")
            else:
                st.error("❌ Weak Password - Improve it using the suggestions below")
            
            # Display feedback
            for item in feedback:
                st.write(item)

# Save password button
            st.download_button(
                label="Save Password in pc",
                data=password,
                file_name="generated_password.txt",
                mime="text/plain",
                 key="download_button_1"  # Unique key for this button
            )

# Password generator tab
with tab2:
    st.header("Password Generator")
    
    # Simple options
    length = st.slider("Password Length", 8, 24, 16)
    
    # Character options
    col1, col2 = st.columns(2)
    with col1:
        use_upper = st.checkbox("Uppercase (A-Z)", value=True)
        use_lower = st.checkbox("Lowercase (a-z)", value=True)
    with col2:
        use_digits = st.checkbox("Numbers (0-9)", value=True)
        use_special = st.checkbox("Special (!@#$%^&*)", value=True)
    
    if st.button("Generate Password"):
        # Build character pool
        chars = ""
        if use_upper: chars += string.ascii_uppercase
        if use_lower: chars += string.ascii_lowercase
        if use_digits: chars += string.digits
        if use_special: chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        if not chars:
            st.error("Select at least one character type")
        else:
            # Generate password
            password = ''.join(random.choice(chars) for _ in range(length))
            
            # Display the generated password
            st.code(password)
            st.text_area("Copy password:", password, height=70)
            
            # Save password button
            st.download_button(
                label="Save Password in pc",
                data=password,
                file_name="generated_password.txt",
                mime="text/plain",
                 key="download_button_2"  # Unique key for this button
            )

# Sidebar with app information
st.sidebar.title("🔒 Strong Password Tips")
st.sidebar.markdown("""
    - Use at least 8 characters
    - Mix uppercase, lowercase, numbers, and symbols
    - Don't use personal information
    - Use different passwords for different accounts
    """)
st.sidebar.markdown("Connect with me on :🔗 [LinkedIn](https://www.linkedin.com/in/nida-khurram/)")
