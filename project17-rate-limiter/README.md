# 🚦 Project 17: LLM API Rate Limiter & Queue

## What it does
Handles high volume LLM API requests with rate limiting,
automatic retry logic and exponential backoff.

## Key Features
- Tracks requests per minute automatically
- Exponential backoff retry on failures
- Queue management for burst requests
- Full statistics reporting

## Results
- 10/10 requests successful
- 0 failures, 0 retries
- Completed in 7.4 seconds

## Connection to Real Work
Mirrors fault-tolerant design patterns implemented at
Texoham AI - "exponential backoff retry logic reducing
system crashes by 30%"

## Tech Used
- Python, Groq API, LLaMA 3.1
- Rate limiting, exponential backoff