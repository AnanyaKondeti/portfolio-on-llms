# 🤖 Project 1: LLM Prompt Tester

## What it does
Tests how different prompt styles affect LLM responses using the same topic.

## Prompt Techniques Used
- Zero-shot prompting
- Persona prompting ("explain like I'm 5")
- Structured prompting ("step by step")

## Key Finding
Same topic, different prompt style = completely different output quality and style.

## Tech Used
- Python, Groq API, LLaMA 3.1
- python-dotenv for secure key management

## How to Run
1. Add your Groq API key to `.env`
2. Run `python main.py`