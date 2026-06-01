import os
from google import genai

# Apni API key yahan se uthaye
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate():
    # Yahan apna prompt likhen
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Hello, how are you?"
    )
    print(response.text)

if __name__ == "__main__":
    generate()
    
