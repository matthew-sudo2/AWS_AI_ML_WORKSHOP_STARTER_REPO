import requests

try:
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": "Hello", "stream": False},
        timeout=10,
    )
    print("SUCCESS: Setup is working")
    print(res.json()["response"][:50])
except Exception as e:
    print("FAILED:", e)
