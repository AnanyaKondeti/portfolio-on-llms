import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def zero_shot(review):
    prompt = f"""Is this review positive or negative? Reply with only one word: positive or negative.
Review: {review}"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().lower()

def few_shot(review):
    prompt = f"""Is this review positive or negative? Reply with only one word: positive or negative.

"I loved it!" → positive
"Terrible experience" → negative
"Best purchase ever!" → positive
"Complete waste of money" → negative

Review: {review} →"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().lower()

tests = [
    ("The product broke after one day", "negative"),
    ("Absolutely love this!", "positive"),
    ("Not worth the price", "negative"),
    ("Exceeded my expectations", "positive"),
    ("Worst experience ever", "negative"),
    ("It's okay I guess", "negative"),
    ("Not bad at all", "positive"),
    ("Could be worse", "negative"),
    ("I've seen better but still fine", "negative"),
    ("Surprisingly not terrible", "positive"),
]

print("=" * 60)
print(f"{'Review':<35} {'Correct':<10} {'Zero-Shot':<12} {'Few-Shot'}")
print("=" * 60)

zero_correct = 0
few_correct = 0

for review, correct in tests:
    zero = zero_shot(review)
    few = few_shot(review)
    if correct in zero: zero_correct += 1
    if correct in few: few_correct += 1
    print(f"{review[:33]:<35} {correct:<10} {zero:<12} {few}")

print("=" * 60)
print(f"Zero-Shot Accuracy: {zero_correct}/{len(tests)}")
print(f"Few-Shot Accuracy:  {few_correct}/{len(tests)}")