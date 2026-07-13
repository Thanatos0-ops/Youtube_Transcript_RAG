from pydantic import BaseModel


class IngestResponse(BaseModel):

    video_id: str
    chunks: int


class QueryResponse(BaseModel):

    answer: str