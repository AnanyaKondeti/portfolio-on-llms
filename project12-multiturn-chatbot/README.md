# 🤖 Project 12: Multi-Turn Chatbot with Memory

## What it does
A career coach chatbot that remembers everything said
across the entire conversation using conversation history.

## Key Feature
Demonstrates short-term memory by passing full conversation
history to LLM on every message.

## Memory Test Result
Bot correctly recalled user's name and experience
when asked later in conversation ✅

## How memory works
Every message is stored in a list and sent to the LLM
each time - LLM reads back the history to "remember"

## Tech Used
- Python, Groq API, LLaMA 3.1
- Conversation history management