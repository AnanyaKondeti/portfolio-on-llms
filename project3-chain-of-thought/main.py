import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def normal_prompt(question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content.strip()

def chain_of_thought(question):
    cot_prompt = f"{question}\nThink through this step by step."
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": cot_prompt}]
    )
    return response.choices[0].message.content.strip()

questions = [
    "If a train travels 120km in 2 hours, how long to travel 450km?",
    "A shirt costs $35 after 30% discount. What was original price?",
    "If 8 workers finish a job in 6 days, how many days for 12 workers?",
]

for q in questions:
    print("\n" + "=" * 60)
    print(f"❓ Question: {q}")
    print("\n📤 Normal Response:")
    print(normal_prompt(q))
    print("\n🧠 Chain of Thought Response:")
    print(chain_of_thought(q))