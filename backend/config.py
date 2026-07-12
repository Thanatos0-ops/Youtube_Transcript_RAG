import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

TRANSCRIPT_DIR = 'data/transcripts'

VECTORSTORE_DIR = 'data/vectorstore'