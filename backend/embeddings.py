from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import GOOGLE_API_KEY


def get_embedding_model():

    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        api_key=GOOGLE_API_KEY
    )

