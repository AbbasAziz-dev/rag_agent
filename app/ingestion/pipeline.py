from ingestion.loader import load_documents
from ingestion.chunker import split_documents
from vectordb.chroma_store import get_vectorstore


def ingest(file_path: str):
    """Load → Split → Store documents"""

    docs = load_documents(file_path)
    chunks = split_documents(docs)

    vectordb = get_vectorstore()

    print("Adding documents:", len(chunks))

    vectordb.add_documents(chunks)
    vectordb.persist()   

    print("✅ Ingestion complete")