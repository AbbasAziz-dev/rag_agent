from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def get_vectorstore():
    """Initialize or load Chroma vector DB."""

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )