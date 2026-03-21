import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat(conversation_history, user_message):
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Send entire history to LLM
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=conversation_history
    )
    
    assistant_message = response.choices[0].message.content.strip()
    
    # Add assistant response to history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message, conversation_history

# System prompt gives the chatbot a persona
system_prompt = {
    "role": "system",
    "content": """You are a helpful AI career coach specializing in 
tech jobs and prompt engineering roles. You remember everything 
the user tells you and refer back to it naturally."""
}

# Start conversation with system prompt
conversation = [system_prompt]

# Simulated multi-turn conversation
exchanges = [
    "Hi! My name is Ananya and I'm looking for a prompt engineer job",
    "I have experience in IoT systems and HCI research",
    "What skills should I focus on?",
    "What was my name again and what experience did I mention?",
    "Can you suggest 3 companies I should apply to?",
]

print("🤖 Multi-Turn Career Coach Chatbot")
print("=" * 60)

for user_input in exchanges:
    print(f"\n👤 User: {user_input}")
    response, conversation = chat(conversation, user_input)
    print(f"🤖 Bot: {response}")
    print(f"📝 Messages in memory: {len(conversation)}")