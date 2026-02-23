import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_structured(text, schema_description):
    prompt = f"""Extract information from the text below and return ONLY a valid JSON object.
No explanation, no markdown, just pure JSON.

Schema needed: {schema_description}

Text: {text}

JSON:"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    
    raw = response.choices[0].message.content.strip()
    
    # Clean and parse JSON
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)

# Test 1: Extract person info
text1 = """
Hi, my name is Sarah Johnson. I'm 28 years old and I work as 
a data scientist at Google in San Francisco. You can reach 
me at sarah.j@gmail.com or call 555-1234.
"""

# Test 2: Extract product info
text2 = """
The iPhone 15 Pro is available for $999. It features a 
6.1 inch display, 256GB storage, and comes in black, 
white and gold colors. Currently in stock.
"""

# Test 3: Extract job posting info
text3 = """
We are hiring a Senior Prompt Engineer at Microsoft. 
The role requires 3+ years experience with LLMs, 
Python, and RAG systems. Salary range is $120,000 
to $160,000. Position is remote friendly.
"""

tests = [
    (text1, "name, age, job, company, city, email, phone"),
    (text2, "product_name, price, display_size, storage, colors, in_stock"),
    (text3, "company, role, experience_required, skills, salary_min, salary_max, remote"),
]

for text, schema in tests:
    print("\n" + "=" * 60)
    print(f"📄 Input Text: {text.strip()[:80]}...")
    print(f"\n✅ Extracted JSON:")
    result = extract_structured(text, schema)
    print(json.dumps(result, indent=2))