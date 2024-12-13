from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

def get_qa_chain() -> load_qa_chain:
    """
    Load and return the QA chain.
    """
    return load_qa_chain(OpenAI(), chain_type="stuff")

def answer_query(chain, document_search, query: str) -> str:
    """
    Perform a similarity search and get the answer to the query.
    """
    docs = document_search.similarity_search(query)
    return chain.run(input_documents=docs, question=query)