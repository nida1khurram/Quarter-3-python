
import os 
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

# ✅ Correct: Initialize the model properly
model = genai.GenerativeModel("gemini-2.0-flash")

@cl.on_chat_start
async def start_chat():
    await cl.Message(content="Hello! How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    # ✅ Correct: Use generate_content() to get a response
    response = model.generate_content(message.content)
    await cl.Message(content=response.text).send()
