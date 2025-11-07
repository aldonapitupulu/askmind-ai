import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key dari file .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Inisialisasi model Gemini
model = genai.GenerativeModel("gemini-2.5-flash")

# Tes prompt sederhana
response = model.generate_content("Hai! Coba jawab singkat, siapa presiden pertama Indonesia?")
print(response.text)