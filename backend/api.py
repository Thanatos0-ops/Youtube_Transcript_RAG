from fastapi import APIRouter
from ingestion import ingest_video
from request_model import IngestRequest, QueryRequest
from response_model import IngestResponse, QueryResponse
from rag import ask


router = APIRouter()


@router.post("/ingest")
def ingest(payload: IngestRequest, response_model= IngestResponse):

    return ingest_video(payload.source)


@router.post("/query")
def query(payload: QueryRequest):

    answer = ask(payload.question)
    
    return QueryResponse(answer = answer)