import streamlit as st
import requests


BACKEND_URL = "http://localhost:8000"

st.title("Youtube Transcript RAG")

# Ingest Section

st.header("1. Add Youtube Video")

source = st.text_input("Enter Youtube Video ID or URL")

if st.button("Ingest Video"):

    response = requests.post(
        f"{BACKEND_URL}/ingest",
        json={
            "source": source
        }
    )

if response.status_code == 200:

    data = response.json()

    st.success(
        f"Video ingested successfully."
        f"Created {data['chunks']} chunks."
    )

else:

    st.error("response.text")



# Query Section

st.header("2. Ask Questions")

question = st.text_input("Ask something about the video")


if st.button("Ask"):

    response.requests.post(
        f"{BACKEND_URL}/query",
        json={
            "question": question
        }
    )

if response.status_code == 200:

    data = response.json()

    st.write("### Answer")
    st.write(data['answer'])

else:

    st.error(response.text)