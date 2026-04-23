import streamlit as st
import requests

st.title("Local LLM Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Enter your message:")

if user_input:
    st.session_state.messages.append(("user", user_input))

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": user_input, "stream": False},
        )
        reply = response.json()["response"]
    except:
        reply = "Error: Make sure Ollama is running"

    st.session_state.messages.append(("bot", reply))

for role, msg in st.session_state.messages:
    st.write(f"**{role}:** {msg}")
