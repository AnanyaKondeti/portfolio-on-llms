import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

HEURISTICS = [
    "Visibility of system status",
    "Match between system and real world",
    "User control and freedom",
    "Consistency and standards",
    "Error prevention",
    "Recognition rather than recall",
    "Flexibility and efficiency of use",
    "Aesthetic and minimalist design",
    "Help users recognize and recover from errors",
    "Help and documentation"
]

def analyze_app(app_description):
    heuristics_list = "\n".join([f"{i+1}. {h}" for i, h in enumerate(HEURISTICS)])
    
    prompt = f"""You are a UX expert. Analyze this app description against Nielsen's 10 Heuristics.

App Description: {app_description}

Nielsen's 10 Heuristics:
{heuristics_list}

For each heuristic give:
- Score: 1-5
- Issue: what's wrong (if any)
- Suggestion: how to improve

Format each as:
[Heuristic name]: Score X/5 | Issue: ... | Suggestion: ..."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Test with a sample app
app = """
A food delivery app where users browse restaurants. 
There is no loading indicator when searching. 
Errors just show a code like 'Error 404'. 
No undo option after placing order.
The interface has 15 menu items on the home screen.
"""

print("🔍 HCI Usability Analysis")
print("=" * 60)
print(f"App Description: {app.strip()}")
print("=" * 60)
print("\n📊 Analysis Results:\n")
print(analyze_app(app))