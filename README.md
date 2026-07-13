# Youtube_Transcript_RAG# YouTube Transcript RAG

A Retrieval-Augmented Generation (RAG) application that allows users to interact with YouTube video transcripts using Large Language Models (LLMs).

The application extracts transcripts from YouTube videos, processes the text into chunks, generates embeddings using Google's Gemini embedding model, stores them in a FAISS vector database, and retrieves relevant context to answer user queries.

---

## Features

- Extract transcripts from YouTube videos
- Automatic text chunking
- Semantic search using FAISS vector database
- Gemini-powered embeddings and responses
- Retrieval-Augmented Generation pipeline
- FastAPI backend API
- Streamlit interactive frontend

---

# System Architecture

The overall workflow is:

$$
\text{YouTube Video}
\rightarrow
\text{Transcript Extraction}
\rightarrow
\text{Text Chunking}
\rightarrow
\text{Embedding Generation}
\rightarrow
\text{FAISS Vector Store}
\rightarrow
\text{Similarity Retrieval}
\rightarrow
\text{Gemini LLM Response}
$$

Architecture flow:

```
                  YouTube Video
                       |
                       v
          youtube-transcript-api
                       |
                       v
              Transcript Data
                       |
                       v
          Text Splitter / Chunking
                       |
                       v
          Gemini Embedding Model
                       |
                       v
               FAISS Vector DB
                       |
                       v
             Relevant Context Retrieval
                       |
                       v
                 Gemini LLM
                       |
                       v
              Final User Response
```

---

# Project Structure

```
Youtube_Transcript_RAG/
│
├── backend/
│   ├── app.py
│   └── ...
│
├── frontend/
│   ├── app.py
│   └── ...
│
├── requirements.txt
├── README.md
└── .env
```

---

# Requirements

Before running the project, make sure you have:

- Python 3.10 or higher
- Google Gemini API key
- Internet connection for fetching YouTube transcripts

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Thanatos0-ops/Youtube_Transcript_RAG.git

cd Youtube_Transcript_RAG
```

---

## Create Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# Install Dependencies

The project dependencies are maintained in the root `requirements.txt` file.

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root directory:

```
GOOGLE_API_KEY=your_gemini_api_key
```

Replace:

```
your_gemini_api_key
```

with your actual Google Gemini API key.

---

# Running the Application

The backend and frontend run as separate services.

Open two terminal windows.

---

# Backend (FastAPI)

Navigate to the backend directory:

```bash
cd backend
```

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The backend will run at:

```
http://127.0.0.1:8000
```

---

# Frontend (Streamlit)

Open another terminal:

Navigate to the frontend directory:

```bash
cd frontend
```

Run Streamlit:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# Dependencies

Main libraries used:

```text
fastapi
uvicorn
streamlit

langchain
langchain-community
langchain-google-genai
langchain-text-splitters

faiss-cpu

youtube-transcript-api

python-dotenv
pydantic
requests

google-generativeai
numpy
```

---

# RAG Pipeline Explanation

The application follows the following pipeline:

$$
Query
\rightarrow
Embedding
\rightarrow
FAISS Similarity Search
\rightarrow
Relevant Transcript Chunks
\rightarrow
LLM Generation
\rightarrow
Answer
$$

The retrieved transcript chunks provide context to the Gemini model, reducing hallucination and improving answer relevance.

---

# Troubleshooting

## Transcript Not Available

Some YouTube videos do not provide captions. Ensure the video has available transcripts.

---

## Gemini API Error

Check:

1. Your API key is valid
2. The `.env` file exists
3. The environment variable name is:

```
GOOGLE_API_KEY
```

---

## Module Import Error

Make sure dependencies are installed from the root directory:

```bash
pip install -r requirements.txt
```

---

# Future Improvements

Possible improvements:

- Persistent FAISS storage
- Chat history support
- Multiple video collections
- Authentication system
- Docker deployment
- Automated testing
- Cloud deployment

---

# License

This project is open-source and available for learning and development purposes.