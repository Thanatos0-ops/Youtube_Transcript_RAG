from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from transcript import extract_video_id, fetch_transcript
from vectorstore import create_vectorstore
from config import TRANSCRIPT_DIR


def ingest_video(source: str):
    
    video_id = extract_video_id(source)

    transcript = fetch_transcript(video_id)

    save_transcript(video_id, transcript)

    chunks = split_transcript(transcript)

    create_vectorstore(chunks)

    return {"video_id": video_id, "chunks": len(chunks)}


def save_transcript(video_id, text):

    Path(TRANSCRIPT_DIR).mkdir(parents=True, exist_ok=True)

    file_path = (f"{TRANSCRIPT_DIR}/{video_id}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)


def split_transcript(transcript):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000, 
        chunk_overlap = 200
    )

    chunks = splitter.split_text(transcript)

    return [
        Document(
            page_content=chunk,
            metadata ={"source": "youtube"}
        )
        for chunk in chunks
    ]