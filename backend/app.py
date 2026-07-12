from fastapi import FastAPI
from api import router

app = FastAPI()

app = FastAPI(
    title="Youtube Transcript RAG"
)

app.include_router(router)