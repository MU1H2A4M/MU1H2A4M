import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
print(API_KEY)

def get_gemini_response(prompt):
    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=(API_KEY)"
