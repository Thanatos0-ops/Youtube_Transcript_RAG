from fastapi import APIRouter
from ingestion import ingest_video
from rag import ask


router = APIRouter()


@router.post("/ingest")
def ingest(payload: dict):

    source = (
        payload.get("video_url") or payload.get("video_id")
    )
    
    return ingest_video(source)


@router.post("/query")
def query(payload: dict):
    
    return {
        "answer": ask(payload["question"])
    }