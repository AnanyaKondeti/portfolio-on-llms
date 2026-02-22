import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def evaluate_response(question, response):
    prompt = f"""You are an LLM response evaluator. Score this response on 5 criteria.

Question: {question}
Response: {response}

Score each criteria from 1-10 and explain why:
1. Relevance: Does it answer the question?
2. Accuracy: Is the information correct?
3. Completeness: Is anything important missing?
4. Clarity: Is it easy to understand?
5. Conciseness: Is it the right length?

Format exactly like this:
Relevance: X/10 | Reason: ...
Accuracy: X/10 | Reason: ...
Completeness: X/10 | Reason: ...
Clarity: X/10 | Reason: ...
Conciseness: X/10 | Reason: ...
Total: X/50
Overall: one sentence summary"""

    response_eval = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response_eval.choices[0].message.content.strip()

# Test with different quality responses
tests = [
    {
        "question": "What is Python?",
        "response": "Python is a programming language.",
        "label": "Too Short"
    },
    {
        "question": "What is Python?",
        "response": "Python is a high-level, beginner-friendly programming language used for web development, data science, and AI. Created by Guido van Rossum in 1991, it emphasizes code readability.",
        "label": "Good Response"
    },
    {
        "question": "What is Python?",
        "response": "Python is a snake found in tropical regions. It can grow up to 30 feet long.",
        "label": "Wrong Answer"
    },
]

for test in tests:
    print(f"\n{'='*60}")
    print(f"📝 Label: {test['label']}")
    print(f"❓ Question: {test['question']}")
    print(f"💬 Response: {test['response']}")
    print(f"\n📊 Evaluation:")
    print(evaluate_response(test['question'], test['response']))