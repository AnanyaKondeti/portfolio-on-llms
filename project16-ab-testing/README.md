# 🧪 Project 16: Prompt A/B Testing Dashboard

## What it does
Automatically compares two prompt versions across multiple
test inputs and scores them using LLM-as-judge.

## Key Finding
Simple prompt (A) scored 24/30 vs structured prompt (B) 23/30
Shows that more complex prompts don't always win!

## How it works
1. Run both prompts on same inputs
2. Score each response automatically
3. Compare scores across all tests
4. Declare overall winner based on data

## Why it matters
MNC prompt engineers use A/B testing to make data-driven
decisions about which prompts to deploy in production.

## Tech Used
- Python, Groq API, LLaMA 3.1
- LLM-as-judge scoring