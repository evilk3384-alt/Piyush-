import os
from google.genai import Client

# API Key setup
client = Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate():
    # Naye SDK ka sahi syntax
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Hello, how are you?"
    )
    print(response.text)

if __name__ == "__main__":
    generate()
    
