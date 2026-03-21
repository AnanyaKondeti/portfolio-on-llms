import os
import time
import random
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class RateLimiter:
    def __init__(self, max_requests_per_minute=10):
        self.max_requests = max_requests_per_minute
        self.requests = []
        self.total_success = 0
        self.total_failed = 0
        self.total_retries = 0

    def can_make_request(self):
        now = time.time()
        # Remove requests older than 1 minute
        self.requests = [r for r in self.requests if now - r < 60]
        return len(self.requests) < self.max_requests

    def add_request(self):
        self.requests.append(time.time())

def call_llm_with_retry(prompt, rate_limiter, max_retries=3):
    for attempt in range(max_retries):
        # Check rate limit
        if not rate_limiter.can_make_request():
            wait_time = 60 - (time.time() - rate_limiter.requests[0])
            print(f"⏳ Rate limit reached! Waiting {wait_time:.1f}s...")
            time.sleep(wait_time + 1)

        try:
            # Exponential backoff delay
            if attempt > 0:
                wait = 2 ** attempt + random.uniform(0, 1)
                print(f"🔄 Retry {attempt}/{max_retries} - waiting {wait:.1f}s...")
                rate_limiter.total_retries += 1
                time.sleep(wait)

            rate_limiter.add_request()
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )
            rate_limiter.total_success += 1
            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"❌ Attempt {attempt + 1} failed: {str(e)[:50]}")
            rate_limiter.total_failed += 1
            if attempt == max_retries - 1:
                return f"Failed after {max_retries} attempts"

# Create rate limiter
rate_limiter = RateLimiter(max_requests_per_minute=10)

# Simulate 10 concurrent requests
prompts = [
    "What is Python in one sentence?",
    "What is machine learning in one sentence?",
    "What is RAG in one sentence?",
    "What is prompt engineering in one sentence?",
    "What is an API in one sentence?",
    "What is a neural network in one sentence?",
    "What is fine tuning in one sentence?",
    "What is a vector database in one sentence?",
    "What is LangChain in one sentence?",
    "What is a token in LLMs in one sentence?",
]

print("🚦 LLM Rate Limiter & Queue System")
print("=" * 60)
print(f"📊 Max requests per minute: {rate_limiter.max_requests}")
print(f"📝 Total requests to process: {len(prompts)}")
print("=" * 60)

start_time = time.time()

for i, prompt in enumerate(prompts):
    print(f"\n📤 Request {i+1}: {prompt}")
    response = call_llm_with_retry(prompt, rate_limiter)
    print(f"✅ Response: {response[:100]}")
    time.sleep(0.5)

end_time = time.time()

print("\n" + "=" * 60)
print("📊 Final Statistics:")
print(f"✅ Successful requests: {rate_limiter.total_success}")
print(f"❌ Failed requests: {rate_limiter.total_failed}")
print(f"🔄 Total retries: {rate_limiter.total_retries}")
print(f"⏱️ Total time: {end_time - start_time:.1f}s")