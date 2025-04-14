# https://knai-secure-data.streamlit.app/
# Import required libraries
import streamlit as st  # Web app framework
import hashlib  # Password hashing
from cryptography.fernet import Fernet  # Encryption/decryption
from datetime import datetime, timedelta  # For lockout timer
import os  # Environment variables
import base64  # Key encoding
import json  # Data storage
from pathlib import Path  # File path handling

# Hide the GitHub icon
st.set_page_config(menu_items={'About': None})

# ========== CONFIGURATION ==========
DATA_FILE = "secure_data.json"  # File to store encrypted data
MASTER_PASSWORD = os.getenv("MASTER_PASSWORD", "admin123")  # Default password

# ========== SESSION STATE SETUP ==========
# Initialize data storage
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}
    # Load existing data if file exists
    if Path(DATA_FILE).exists():
        with open(DATA_FILE) as f:
            st.session_state.stored_data = json.load(f)

# Track failed login attempts
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

# Track lockout expiration time
if 'lockout_time' not in st.session_state:
    st.session_state.lockout_time = None

# Track authentication state
if 'needs_login' not in st.session_state:
    st.session_state.needs_login = True

# ========== SECURITY FUNCTIONS ==========
def get_key(passkey):
    """Generate Fernet-compatible key from passkey"""
    return base64.urlsafe_b64encode(hashlib.sha256(passkey.encode()).digest())

def encrypt(text, passkey):
    """Encrypt text using passkey-derived key"""
    return Fernet(get_key(passkey)).encrypt(text.encode()).decode()

def decrypt(encrypted_text, passkey):
    """Decrypt text with security checks and lockout"""
    # Check if account is locked
    if st.session_state.lockout_time and datetime.now() < st.session_state.lockout_time:
        st.error(f"🔒 Locked. Try again in {(st.session_state.lockout_time - datetime.now()).seconds}s")
        return None
    
    try:
        # Attempt decryption
        return Fernet(get_key(passkey)).decrypt(encrypted_text.encode()).decode()
    except:
        # Handle failed attempts
        st.session_state.failed_attempts += 1
        if st.session_state.failed_attempts >= 3:  # Lock after 3 attempts
            st.session_state.lockout_time = datetime.now() + timedelta(seconds=30)
            st.error("🔒 Locked for 30 seconds")
        return None

# ========== MAIN APP ==========
st.title("🔒 Secure Data Storage")

# ========== AUTHENTICATION ==========
if st.session_state.needs_login or (st.session_state.failed_attempts >= 3 and 
                                   (not st.session_state.lockout_time or 
                                    datetime.now() >= st.session_state.lockout_time)):
    st.subheader("🔑 Login")
    # Password input and check
    if st.text_input("Master Password:", type="password", key="pw") == MASTER_PASSWORD:
        # Reset security state on successful login
        st.session_state.failed_attempts = 0
        st.session_state.lockout_time = None
        st.session_state.needs_login = False
        st.rerun()  # Refresh to show main app
    elif st.button("Login"):
        st.error("❌ Incorrect password!")
    st.write("Master Password For Testing:🔑admin123")
# ========== AUTHENTICATED INTERFACE ==========
else:
    # Navigation menu
    menu = st.sidebar.selectbox("Menu", ["📁 Store", "🔍 Retrieve", "⚙️ Info"])
    
    # ===== STORE DATA =====
    if menu == "📁 Store":
        st.subheader("Store Data")
        data = st.text_area("Data to encrypt:")
        passkey = st.text_input("Passkey:", type="password", key="pk")
        
        if st.button("Encrypt") and data and passkey:
            # Create unique ID and store encrypted data
            id = f"entry_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            st.session_state.stored_data[id] = {
                "encrypted_text": encrypt(data, passkey),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            # Save to file
            with open(DATA_FILE, 'w') as f:
                json.dump(st.session_state.stored_data, f)
            st.success("✅ Stored!")
    
    # ===== RETRIEVE DATA =====
    elif menu == "🔍 Retrieve":
        st.subheader("Retrieve Data")
        if st.session_state.stored_data:
            # Select entry to decrypt
            selected = st.selectbox("Select:", list(st.session_state.stored_data.keys()))
            # Decrypt and show if successful
            decrypted = decrypt(st.session_state.stored_data[selected]["encrypted_text"], 
                              st.text_input("Passkey:", type="password", key="dpk"))
            if decrypted:
                st.text_area("Content:", decrypted, height=200)
    
    # ===== SYSTEM INFO =====
    elif menu == "⚙️ Info":
        st.write(f"Entries: {len(st.session_state.stored_data)}")  # Show entry count
    
    # Logout button
    if st.sidebar.button("🚪 Logout"):
        st.session_state.needs_login = True
        st.rerun()


