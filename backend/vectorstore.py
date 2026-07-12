from langchain_community.vectorstores import FAISS
from embeddings import get_embedding_model
from config import VECTORSTORE_DIR


def create_vectorstore(document):

    db = FAISS.from_documents(document, get_embedding_model())

    db.save_local(VECTORSTORE_DIR)

    return db


def load_vectorstore():

    return FAISS.load_local(
        VECTORSTORE_DIR,
        get_embedding_model(),
        allow_dangerous_deserialization=True
    )