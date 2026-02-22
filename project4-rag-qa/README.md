# 📚 Project 4: RAG Document Q&A

## What it does
Implements Retrieval Augmented Generation (RAG) to answer questions 
from custom documents using semantic search.

## How it works
1. Documents are converted to vector embeddings using SentenceTransformers
2. User question is also converted to a vector
3. FAISS finds the most similar documents
4. LLM answers using only the retrieved context

## Why RAG matters
Companies use RAG to use LLMs on private data without sending 
it to external APIs - used in almost every enterprise LLM project.

## Tech Used
- Python, Groq API, LLaMA 3.1
- FAISS for vector search
- SentenceTransformers for embeddings