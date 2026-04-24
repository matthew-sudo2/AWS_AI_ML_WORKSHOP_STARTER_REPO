import requests

# This script checks if Ollama is running and if the llama3 model is available.
# It is a simple tool for workshop participants to debug their setup.

URL = "http://localhost:11434/api/generate"
MODEL = "llama3:8b"

try:
    print(f"Connecting to Ollama at {URL}...")
    res = requests.post(
        URL,
        json={"model": MODEL, "prompt": "Say 'Ollama is ready!'", "stream": False},
        timeout=60,
    )
    res.raise_for_status()
    
    print("\n[SUCCESS] Everything is set up correctly!")
    print(f"Model response: {res.json()['response']}")

except requests.exceptions.ConnectionError:
    print("\n[FAILED] Could not connect to Ollama.")
    print("Is the Ollama application running? Check your system tray.")
except requests.exceptions.HTTPError as e:
    print(f"\n[FAILED] Model '{MODEL}' not found.")
    print(f"Run 'ollama pull {MODEL}' in your terminal first.")
except Exception as e:
    print(f"\n[FAILED] An unexpected error occurred: {e}")
