import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_algorithm(algorithm_name):
    prompt = f"""You are an expert computer science professor. 
Explain the {algorithm_name} algorithm in this exact format:

## Overview
Brief description of what it does

## How it works (Step by Step)
Numbered steps explaining the algorithm

## Pseudocode
Clean pseudocode implementation

## Time & Space Complexity
- Time: O(?)
- Space: O(?)
- Explanation of why

## Real World Example
A practical real world use case

## Fun Fact
One interesting fact about this algorithm"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Test with algorithms from Ananya's resume!
algorithms = [
    "Ford-Fulkerson Maximum Flow",
    "Dijkstra's Shortest Path",
    "Binary Search",
]

for algo in algorithms:
    print(f"\n{'='*60}")
    print(f"🔍 Algorithm: {algo}")
    print(f"{'='*60}")
    print(explain_algorithm(algo))