from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    """Split documents into smaller chunks for embedding."""
    
        chunk_overlap=400
        chunk_overlap=600
    )

    return splitter.split_documents(documents)