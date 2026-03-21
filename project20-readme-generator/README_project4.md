**RAG Document Q&A 🤖**
======================

A Retrieval Augmented Generation (RAG) based question answering system designed for efficient and accurate knowledge retrieval.

## What it does
----------------

RAG Document Q&A is a cutting-edge question answering system that leverages the power of Retrieval Augmented Generation (RAG) to retrieve and generate context-aware answers from a large document dataset. By utilizing vector embeddings and semantic search, our system enables fast and accurate knowledge retrieval, making it an ideal solution for applications that require efficient and reliable information retrieval.

## Key Features
---------------

* **Vector embeddings**: Leverages SentenceTransformers to generate dense vector embeddings for efficient similarity search.
* **Semantic search**: Utilizes FAISS for fast and accurate similarity search to retrieve relevant documents.
* **Context-aware answers**: Utilizes Groq API with RAG to generate context-aware answers based on the retrieved documents.
* **Efficient knowledge retrieval**: Designed to handle large document datasets and provide fast response times.

## How to Run
-------------

### Prerequisites

* Python 3.8+
* Groq API
* FAISS
* SentenceTransformers

### Installation

```bash
pip install -r requirements.txt
```

### Running the System

```bash
python main.py
```

### Example Usage

Run the following command to query the system:
```
curl -X POST \
  http://localhost:5000/query \
  -H 'Content-Type: application/json' \
  -d '{"question": "What is the capital of France?"}'
```

### API Documentation

For detailed API documentation, please refer to the [API Documentation](docs/api.md) section.

## Tech Stack
------------

* **Programming Language**: Python
* **Technologies**:
	+ Groq API: For RAG-based answer generation
	+ FAISS: For efficient similarity search
	+ SentenceTransformers: For vector embeddings
* **Dependencies**:
	+ Python: 3.8+
	+ Groq API: >= 1.0.0
	+ FAISS: >= 1.8.0
	+ SentenceTransformers: >= 1.5.0

## What I Learned
---------------

During the development of this project, I gained hands-on experience with the following concepts:

* Retrieval Augmented Generation (RAG) for context-aware answer generation
* Efficient similarity search using FAISS
* Utilizing vector embeddings for semantic search
* Integrating Groq API with RAG for answer generation

Note to Recruiters:
This project demonstrates my expertise in leveraging cutting-edge technologies to build efficient and accurate question answering systems. I'm excited to bring my skills to a forward-thinking team where I can continue to innovate and push the boundaries of AI-powered solutions.