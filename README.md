# PDF Query System

## Overview

The PDF Query System is a modularized Python application that allows users to query the contents of a PDF document using natural language. It leverages:

- LangChain for managing document processing, embeddings, and QA chains.

- FAISS for efficient vector similarity search.

- Streamlit for a user-friendly web-based frontend.

- OpenAI Embeddings for encoding textual data into embeddings suitable for similarity search.

With this system, users can upload a PDF, extract its content, and ask questions about it to get concise, relevant answers.

## Features

1) PDF Text Extraction: Extracts text content from uploaded PDF documents.

2) Text Splitting: Splits the text into smaller, manageable chunks for better embedding performance.

3) Embedding and Vector Store: Creates embeddings for each text chunk and stores them in a FAISS index.

4) Similarity Search: Finds the most relevant chunks for a given query using vector similarity.

5) QA Chain: Uses OpenAI's GPT model to generate answers based on the retrieved chunks.

6) Streamlit Frontend: Provides an interactive interface for uploading PDFs and querying their content.

## Installation

### Clone the repository:

``` bash 
git clone https://github.com/your-username/pdf-query-system.git
cd pdf-query-system 
```

### Create a virtual environment and activate it:

``` bash 
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Set up your OpenAI API key:

```bash
export OPENAI_API_KEY="your-openai-api-key"   

# On Windows: 
set OPENAI_API_KEY="your-openai-api-key"
```

## Usage

```bash
#Run the Streamlit app:

streamlit run main.py
```

- Open the app in your browser at http://localhost:8501.

- Upload a PDF document and ask questions in natural language.

## Demo Video

https://drive.google.com/file/d/1JB3IGo0bm2HuNWkJN31WG9hFF9vJ4_sp

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

1) OpenAI for their powerful GPT and embedding models.

2) LangChain for providing seamless tools for working with LLMs.

3) FAISS for efficient similarity search.

4) Streamlit for an easy-to-use frontend.


