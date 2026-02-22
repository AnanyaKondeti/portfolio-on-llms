import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def tailor_resume(job_description, resume_bullets):
    prompt = f"""You are an expert resume writer. Rewrite these resume bullet points 
to better match the job description below.

Keep the same facts and experiences but use language and keywords from the job description.
Make each bullet point stronger and more relevant.

Job Description:
{job_description}

Original Resume Bullets:
{resume_bullets}

Rewritten Bullets (keep same number of bullets, make them more relevant):"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Real job description for Prompt Engineer
job_description = """
We are looking for a Prompt Engineer to join our AI team.
Responsibilities include:
- Design and optimize prompts for LLM applications
- Build and evaluate RAG pipelines
- Ensure AI safety and prevent prompt injection attacks
- Work with distributed systems and APIs
- Collaborate with cross-functional teams
Required skills: Python, LLMs, RAG, prompt optimization, AI safety
"""

# Ananya's actual resume bullets
resume_bullets = """
- Developed IoT systems serving 8,000+ daily users with 99.5% uptime
- Reduced system crashes by 30% through fault-tolerant design patterns
- Collaborated with cross-functional teams in Agile environment
- Optimized firmware achieving 20% reduction in memory footprint
- Implemented CI/CD pipelines reducing deployment cycle time by 25%
"""

print("🎯 Resume Tailor Bot")
print("=" * 60)
print("📋 Job Description:")
print(job_description)
print("=" * 60)
print("📄 Original Resume Bullets:")
print(resume_bullets)
print("=" * 60)
print("✨ Tailored Resume Bullets:")
print(tailor_resume(job_description, resume_bullets))