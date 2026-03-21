import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def persona_prompt(question, persona):
    prompt = f"""You are {persona}. 
Answer this question completely in character, using vocabulary, 
tone and examples that match your persona.

Question: {question}"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Same question, 5 different personas
question = "What is machine learning?"

personas = [
    "a pirate from the 1700s",
    "a 5 year old child",
    "a Harvard professor of Computer Science",
    "a sports commentator",
    "a chef at a 5-star restaurant",
]

print("🎭 Persona Prompting Experiment")
print(f"❓ Question: {question}")
print("=" * 60)

for persona in personas:
    print(f"\n🎭 Persona: {persona.upper()}")
    print("-" * 60)
    print(persona_prompt(question, persona))
    print()