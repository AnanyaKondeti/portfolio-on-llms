# 🛡️ Project 5: Prompt Injection Defense Tool

## What it does
Detects and blocks malicious prompt injection attacks before 
they reach the LLM.

## Attack Types Detected
- Instruction override ("ignore previous instructions")
- Role hijacking ("you are now", "pretend you are")
- System prompt extraction ("reveal your instructions")
- Jailbreak attempts ("DAN mode")

## How it works
Pattern matching scans user input before sending to LLM.
Malicious requests are blocked immediately.

## Why it matters
Prompt injection is a top security concern for enterprise 
LLM deployments at MNCs.

## Tech Used
- Python, Groq API, LLaMA 3.1