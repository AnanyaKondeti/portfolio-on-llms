# 🤖 Project 8: ReAct Agent with Tools

## What it does
Implements a ReAct (Reasoning + Acting) agent that decides 
which tool to use based on the question.

## Tools Available
- 🧮 Calculator: math expressions
- 🌡️ Weather: city weather lookup
- 📚 Dictionary: word definitions

## How ReAct works
1. Agent receives question
2. Reasons about which tool to use
3. Uses tool and gets result
4. Answers using tool result

## Key Difference from RAG
RAG searches documents. ReAct actively decides 
which action to take — much more flexible!

## Tech Used
- Python, Groq API, LLaMA 3.1