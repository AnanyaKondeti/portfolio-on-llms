import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_prompt(prompt_template, input_text):
    full_prompt = prompt_template.replace("{input}", input_text)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": full_prompt}]
    )
    return response.choices[0].message.content.strip()

def score_response(question, response):
    prompt = f"""Score this response from 1-10 on overall quality.
Question: {question}
Response: {response}
Reply with ONLY a number between 1-10."""

    result = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    try:
        return int(result.choices[0].message.content.strip()[0])
    except:
        return 5

# Define Prompt A and Prompt B
prompt_a = "Summarize this text: {input}"

prompt_b = """Summarize this text in exactly 3 bullet points.
Focus on the most important facts only.
Be concise and clear.
Text: {input}"""

# Test inputs
test_inputs = [
    """Artificial intelligence is transforming industries worldwide. 
    Companies are using AI for customer service, data analysis, 
    and product development. However, concerns about job displacement 
    and ethical issues remain significant challenges.""",
    
    """Climate change is causing rising sea levels, extreme weather 
    events, and biodiversity loss. Scientists warn that immediate 
    action is needed to reduce carbon emissions. Renewable energy 
    adoption is increasing but not fast enough.""",
    
    """Python is one of the most popular programming languages today. 
    It's used in web development, data science, AI, and automation. 
    Its simple syntax makes it beginner friendly while being powerful 
    enough for complex applications."""
]

print("🧪 Prompt A/B Testing Dashboard")
print("=" * 60)
print(f"📝 Prompt A: {prompt_a}")
print(f"📝 Prompt B: {prompt_b[:50]}...")
print("=" * 60)

a_total = 0
b_total = 0

for i, text in enumerate(test_inputs):
    print(f"\n📄 Test {i+1}:")
    print(f"Input: {text[:60]}...")
    
    response_a = run_prompt(prompt_a, text)
    response_b = run_prompt(prompt_b, text)
    
    score_a = score_response(text, response_a)
    score_b = score_response(text, response_b)
    
    a_total += score_a
    b_total += score_b
    
    print(f"\n🅰️  Prompt A Response:\n{response_a}")
    print(f"⭐ Score A: {score_a}/10")
    print(f"\n🅱️  Prompt B Response:\n{response_b}")
    print(f"⭐ Score B: {score_b}/10")
    
    winner = "🅰️ A" if score_a > score_b else "🅱️ B" if score_b > score_a else "🤝 Tie"
    print(f"🏆 Winner: {winner}")

print("\n" + "=" * 60)
print(f"📊 Final Results:")
print(f"🅰️  Prompt A Total Score: {a_total}/30")
print(f"🅱️  Prompt B Total Score: {b_total}/30")
overall_winner = "🅰️ Prompt A" if a_total > b_total else "🅱️ Prompt B" if b_total > a_total else "🤝 Tie"
print(f"🏆 Overall Winner: {overall_winner}")