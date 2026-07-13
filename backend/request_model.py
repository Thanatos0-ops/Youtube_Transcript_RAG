from pydantic import BaseModel, Field
from typing import Optional


class IngestRequest(BaseModel):

    source: str = Field(description="Enter Youtube video_id or url")
    


class QueryRequest(BaseModel):

    question: str = Field(description="User query goes here")
