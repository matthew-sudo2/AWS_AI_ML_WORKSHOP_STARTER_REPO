import streamlit as st
import requests
import json

# ==========================================
# 1. Page Configuration & UI Setup
# ==========================================
st.set_page_config(
    page_title="Antigravity: Local LLM Workshop",
    page_icon="🤖",
    layout="centered"
)

# --- Sidebar: Tutorial & Settings ---
with st.sidebar:
    st.title("Workshop Guide")
    
    # Simple Tutorial Section
    with st.expander("📖 Instructions", expanded=True):
        st.markdown("""
        **Step 1: Install Ollama**
        Download from [ollama.com](https://ollama.com)
        
        **Step 2: Pull the Model**
        Run this in your terminal:
        `ollama pull llama3:8b`
        
        **Step 3: Run the Model**
        Ensure the Ollama app is running in the background.
        
        **Step 4: Connect**
        This app connects to `localhost:11434`.
        """)

    st.divider()
    
    st.header("⚙️ Model Parameters")
    
    # System Prompt: This tells the LLM how to behave
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful AI assistant.",
        help="Change this to give the assistant a specific role (e.g., 'You are a pirate')."
    )
    
    # Hyperparameters for the model
    temperature = st.slider(
        "Temperature", 
        min_value=0.0, 
        max_value=2.0, 
        value=0.7, 
        step=0.1,
        help="Higher = more creative, Lower = more predictable."
    )
    
    top_p = st.slider(
        "Top P", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.9, 
        step=0.05,
        help="Controls the diversity of the response."
    )
    
    # Button to reset conversation
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# ==========================================
# 2. Chat Logic & History Management
# ==========================================
st.title("Local LLM Chatbot")
st.caption("A beginner-friendly template for the Antigravity Workshop")

# Initialize chat history in Streamlit's session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all messages from the history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# 3. Handling User Input & API Request
# ==========================================
if prompt := st.chat_input("Type your message here..."):
    
    # 1. Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 2. Save user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 3. Prepare the data for Ollama API
    # We use the /api/chat endpoint which takes a list of messages
    payload = {
        "model": "llama3:8b",
        "messages": [
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        "stream": False,  # Set to True for real-time typing effect (advanced)
        "options": {
            "temperature": temperature,
            "top_p": top_p
        }
    }

    # 4. Send request to local Ollama server
    try:
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://localhost:11434/api/chat", 
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            
            # Extract assistant's reply
            output = response.json()
            assistant_reply = output["message"]["content"]
            
        # 5. Display assistant response
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)
            
        # 6. Save assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        
    except requests.exceptions.ConnectionError:
        st.error("Error: Could not connect to Ollama. Make sure it is installed and running!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
