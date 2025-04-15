import streamlit as st
import json, os, time, base64, uuid
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Config
DATA_FILE = "secure_data.json"
MAX_ATTEMPTS, LOCKOUT_TIME = 3, 300  # 5 min lockout
SALT = b"fixed_salt_for_demo"  # In prod, use unique salt per user

# Load/save data
def load_data():
    return json.load(open(DATA_FILE)) if os.path.exists(DATA_FILE) else {"users": {}, "failed_attempts": {}, "lockouts": {}}
data = load_data()
def save_data(): json.dump(data, open(DATA_FILE, "w"))

# Security functions
def get_key(passkey, salt=SALT):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return base64.urlsafe_b64encode(kdf.derive(passkey.encode()))

# User management
def create_user(username, password):
    if username in data["users"]: return False
    data["users"][username] = {
        "hashed_passkey": get_key(password).decode(),
        "encryption_key": Fernet.generate_key().decode(),
        "data": {}
    }
    save_data()
    return True

def authenticate(username, password):
    # Check lockout
    if username in data["lockouts"] and (time.time() - data["lockouts"][username]) < LOCKOUT_TIME:
        st.error(f"Account locked. Try again in {int(LOCKOUT_TIME - (time.time() - data['lockouts'][username]))}s")
        return False
    elif username in data["lockouts"]:
        del data["lockouts"][username]
    
    if username not in data["users"]: return False
    
    if get_key(password).decode() == data["users"][username]["hashed_passkey"]:
        data["failed_attempts"].pop(username, None)
        save_data()
        return True
    
    # Track failed attempts
    data["failed_attempts"][username] = data["failed_attempts"].get(username, 0) + 1
    if data["failed_attempts"][username] >= MAX_ATTEMPTS:
        data["lockouts"][username] = time.time()
        st.error("Too many attempts. Account locked for 5 minutes.")
    save_data()
    return False

# Encryption/decryption
def encrypt(text, username, passkey):
    salt = os.urandom(16)
    cipher = Fernet(get_key(passkey, salt))
    return {
        "encrypted_text": cipher.encrypt(text.encode()).decode(),
        "salt": base64.urlsafe_b64encode(salt).decode()
    }

def decrypt(encrypted_data, username, passkey):
    try:
        salt = base64.urlsafe_b64decode(encrypted_data["salt"].encode())
        cipher = Fernet(get_key(passkey, salt))
        return cipher.decrypt(encrypted_data["encrypted_text"].encode()).decode()
    except: return None

# Streamlit UI
st.title("🔒 Secure Data Encryption")

# Session state
if "authenticated" not in st.session_state:
    st.session_state.update({"authenticated": False, "current_user": None})

# Navigation
menu = ["Login", "Register"] if not st.session_state.authenticated else ["Home", "Store Data", "Retrieve Data", "Logout"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home" and st.session_state.authenticated:
    st.subheader(f"Welcome, {st.session_state.current_user}!")
    st.write(f"🔐 {len(data['users'][st.session_state.current_user]['data'])} stored items")

elif choice == "Login":
    username, password = st.text_input("Username"), st.text_input("Password", type="password")
    if st.button("Login") and authenticate(username, password):
        st.session_state.update({"authenticated": True, "current_user": username})
        st.success("✅ Login successful!")
        st.rerun()

elif choice == "Register":
    user, pwd, confirm = st.text_input("Username"), st.text_input("Password", type="password"), st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if pwd != confirm: st.error("Passwords don't match!")
        elif user in data["users"]: st.error("Username exists!")
        elif create_user(user, pwd): st.success("✅ Account created! Please login."); st.rerun()

elif choice == "Store Data" and st.session_state.authenticated:
    data_id = str(uuid.uuid4())
    user_data = st.text_area("Data:")
    passkey = st.text_input("Passkey for this Data", type="password")
    if st.button("Encrypt & Save") and user_data and passkey:
        data["users"][st.session_state.current_user]["data"][data_id] = encrypt(user_data, st.session_state.current_user, passkey)
        save_data()
        st.success(f"✅ Stored! Data ID: {data_id}")

elif choice == "Retrieve Data" and st.session_state.authenticated:
    items = data["users"][st.session_state.current_user]["data"]
    if not items: st.warning("No stored data")
    else:
        selected = st.selectbox("Select data", list(items.keys()))
        passkey = st.text_input("Passkey", type="password")
        if st.button("Decrypt"):
            decrypted = decrypt(items[selected], st.session_state.current_user, passkey)
            st.text_area("", decrypted, height=200) if decrypted else st.error("❌ Decryption failed")

elif choice == "Logout" and st.session_state.authenticated:
    st.session_state.update({"authenticated": False, "current_user": None})
    st.success("✅ Logged out!"); st.rerun()

# Sidebar status
if st.session_state.authenticated:
    st.sidebar.markdown(f"**User:** {st.session_state.current_user}")
    if st.session_state.current_user in data["failed_attempts"]:
        st.sidebar.warning(f"⚠️ {MAX_ATTEMPTS - data['failed_attempts'][st.session_state.current_user]} attempts left")