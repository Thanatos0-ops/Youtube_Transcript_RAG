import langchain_google_genai
from langchain_google_genai import GoogleGenerativeAI
from config import GOOGLE_API_KEY

def get_llm():
    
    return GoogleGenerativeAI(
        model="gemini-3-flash-preview",
        google_api_key= GOOGLE_API_KEY,
        temperature=0.2
    )