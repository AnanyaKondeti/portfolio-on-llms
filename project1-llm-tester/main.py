import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def test_prompt(prompt):
    print(f"\n📤 Your Prompt: {prompt}")
    print("-" * 50)
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    
    result = response.choices[0].message.content
    print(f"🤖 LLM Response:\n{result}")
    return result

test_prompt("Explain recursion in one sentence")
test_prompt("Explain recursion like I am 5 years old")
test_prompt("Explain recursion step by step with an example")