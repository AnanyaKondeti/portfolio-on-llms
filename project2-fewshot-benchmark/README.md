# 📊 Project 2: Few-Shot vs Zero-Shot Benchmark

## What it does
Compares Zero-Shot vs Few-Shot prompting accuracy on sentiment analysis.

## Key Findings
- Both score 7/10 on tricky reviews
- Few-Shot handles ambiguous phrases better ("Could be worse")
- Neither handles sarcasm well ("Surprisingly not terrible")
- Adding examples helps with ambiguous language

## Prompt Techniques Compared
- Zero-Shot: No examples given
- Few-Shot: 4 examples provided before the question

## Tech Used
- Python, Groq API, LLaMA 3.1
