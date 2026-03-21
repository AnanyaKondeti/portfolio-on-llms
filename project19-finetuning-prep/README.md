# 🔧 Project 19: Fine-Tuning Data Preparation Pipeline

## What it does
Automatically generates training data in JSONL format
for fine-tuning LLMs on custom topics.

## Key Features
- Generates Q&A pairs for any topic automatically
- Converts to JSONL format ready for OpenAI fine-tuning
- Handles parsing errors gracefully
- Scalable to any number of topics

## Output Format
Each line in training_data.jsonl:
{"messages": [{"role": "user", "content": "Q"}, 
{"role": "assistant", "content": "A"}]}

## Results
Generated 9 training pairs across 3 topics:
- Prompt engineering techniques
- RAG and vector databases  
- LLM safety and prompt injection

## Tech Used
- Python, Groq API, LLaMA 3.1
- JSONL format for fine-tuning