import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_qa_pairs(topic):
    prompt = f"""Generate 3 question and answer pairs about "{topic}".

Use EXACTLY this format for each pair:
QUESTION: your question here
ANSWER: your answer here (keep under 50 words)

QUESTION: your question here
ANSWER: your answer here (keep under 50 words)

QUESTION: your question here
ANSWER: your answer here (keep under 50 words)"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    
    raw = response.choices[0].message.content.strip()
    pairs = []
    
    lines = raw.split('\n')
    current_q = None
    
    for line in lines:
        line = line.strip()
        if line.startswith("QUESTION:"):
            current_q = line.replace("QUESTION:", "").strip()
        elif line.startswith("ANSWER:") and current_q:
            answer = line.replace("ANSWER:", "").strip()
            pairs.append({"question": current_q, "answer": answer})
            current_q = None
    
    return pairs

def convert_to_jsonl(qa_pairs, output_file):
    with open(output_file, 'w') as f:
        for pair in qa_pairs:
            training_example = {
                "messages": [
                    {"role": "user", "content": pair["question"]},
                    {"role": "assistant", "content": pair["answer"]}
                ]
            }
            f.write(json.dumps(training_example) + "\n")

topics = [
    "prompt engineering techniques",
    "RAG and vector databases",
    "LLM safety and prompt injection"
]

all_pairs = []

print("🔧 Fine-Tuning Data Preparation Pipeline")
print("=" * 60)

for topic in topics:
    print(f"\n📚 Generating Q&A pairs for: {topic}")
    pairs = generate_qa_pairs(topic)
    all_pairs.extend(pairs)
    print(f"✅ Generated {len(pairs)} pairs")
    for i, pair in enumerate(pairs):
        print(f"\n  Q{i+1}: {pair['question']}")
        print(f"  A{i+1}: {pair['answer'][:100]}...")

output_file = "training_data.jsonl"
convert_to_jsonl(all_pairs, output_file)

print(f"\n{'='*60}")
print(f"✅ Total Q&A pairs: {len(all_pairs)}")
print(f"📄 Saved to: {output_file}")
print(f"\n📋 Sample JSONL:")

with open(output_file, 'r') as f:
    first_line = f.readline()
    print(json.dumps(json.loads(first_line), indent=2))