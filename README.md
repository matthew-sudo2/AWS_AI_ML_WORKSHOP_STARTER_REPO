# 🤖 Antigravity Local LLM Workshop Template

This is a beginner-friendly Streamlit template designed for learning how to build and interact with local Large Language Models (LLMs) using **Ollama**.

## 🎯 Workshop Goals
- Understand how to run LLMs locally.
- Learn how to connect a Python frontend (Streamlit) to an AI backend (Ollama).
- Experiment with model parameters like `System Prompt`, `Temperature`, and `Top P`.

---

## 🛠️ Setup Instructions

### 1. Install Ollama
Download and install Ollama from [ollama.com](https://ollama.com). This acts as your local model server.

### 2. Pull the Model
Open your terminal (Command Prompt or PowerShell) and run:
```bash
ollama pull llama3:8b
```
*Note: This might take a few minutes depending on your internet speed.*

### 3. Setup Python Environment
We recommend using a virtual environment to keep things clean.
```bash
# Create venv
python -m venv venv

# Activate venv (Windows)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Run the Chatbot
Start the Streamlit application:
```bash
streamlit run app.py
```

---

## 🧠 How it Works (The Technical Bit)

### The Backend: Ollama API
Ollama provides a local REST API at `http://localhost:11434`. 
- We use the `/api/chat` endpoint.
- We send a JSON payload containing the model name, message history, and settings.

### The Frontend: Streamlit
Streamlit is used to build the UI entirely in Python.
- **Session State:** `st.session_state` is used to store the chat history so the model "remembers" what you said previously.
- **System Prompt:** This is a hidden instruction sent at the start of every chat to define the AI's behavior.

---

## 🚀 Workshop Challenges
Try these modifications during the workshop:
1. **Change the UI Theme:** Modify the `st.set_page_config` or add custom CSS.
2. **Add a Persona Toggle:** Create a dropdown with preset roles (e.g., "Developer", "Poet", "Grumpy Teacher").
3. **Stream Responses:** Use `stream=True` in the API call to make the text appear word-by-word.
4. **Export Chat:** Add a button to download the chat history as a `.txt` file.

---

*Built with ❤️ for the Antigravity Workshop.*
