# Local LLM Workshop Setup

## 1. Install Requirements

- Install Python 3.10+
- Install Ollama: https://ollama.com

## 1.5. Setup Python Environment

python -m venv venv

## 2. Install Python Dependencies

pip install -r requirements.txt

## 3. Pull Model

ollama pull mistral

## 4. Run Verification

python verify.py

You should see: SUCCESS

## 5. Run App

streamlit run app.py
