import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_code(code, language):
    prompt = f"""You are an expert code reviewer. Review this {language} code and provide feedback on:

1. 🐛 Bugs: Any errors or potential bugs
2. ⚡ Performance: Any performance issues
3. 🔒 Security: Any security vulnerabilities
4. 📖 Readability: Code style and clarity
5. ✅ Suggestions: Specific improvements

Code to review:
```{language}
{code}
```

Give specific line-by-line feedback where relevant."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Test 1: Buggy Python code
code1 = """
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    average = total / len(numbers)
    return average

result = calculate_average([])
print(result)
"""

# Test 2: Insecure code
code2 = """
import sqlite3

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

user = get_user("admin' OR '1'='1")
"""

# Test 3: Performance issue
code3 = """
def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                if lst[i] not in duplicates:
                    duplicates.append(lst[i])
    return duplicates
"""

tests = [
    (code1, "Python", "Division by Zero Bug"),
    (code2, "Python", "SQL Injection Vulnerability"),
    (code3, "Python", "Performance Issue O(n³)"),
]

for code, language, label in tests:
    print(f"\n{'='*60}")
    print(f"🔍 Reviewing: {label}")
    print(f"{'='*60}")
    print(review_code(code, language))