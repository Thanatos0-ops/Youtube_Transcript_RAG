import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent

ROOT_DIR = BASE_DIR.parent

ENV_PATH = ROOT_DIR / ".env"

load_dotenv(ENV_PATH)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

TRANSCRIPT_DIR = 'data/transcripts'

VECTORSTORE_DIR = 'data/vectorstore'

if __name__ == "__main__":

    print(BASE_DIR)
    print(ROOT_DIR)


    print("Looking for:", ENV_PATH)
    print("Exists:", ENV_PATH.exists())

    print("Key exists:", GOOGLE_API_KEY is not None)
    print("Key length:", len(GOOGLE_API_KEY) if GOOGLE_API_KEY else 0)