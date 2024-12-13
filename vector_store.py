from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_vector_store(texts: list) -> FAISS:
    """
    Create a vector store using OpenAI embeddings.
    """
    embeddings = OpenAIEmbeddings()
    document_search = FAISS.from_texts(texts, embeddings)
    return document_search
