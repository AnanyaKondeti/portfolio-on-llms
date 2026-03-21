import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_readme(project_name, description, tech_used, key_features):
    prompt = f"""You are a technical writer. Generate a professional GitHub README for this project.

Project Name: {project_name}
Description: {description}
Tech Used: {tech_used}
Key Features: {key_features}

Generate a complete README with these sections:
# Project Name with emoji
## What it does
## Key Features (bullet points)
## How to Run
## Tech Stack
## What I learned

Make it professional, clear and impressive for recruiters."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def save_readme(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Saved to {filename}")

projects = [
    {
        "name": "LLM Prompt Tester",
        "description": "Tests different prompt styles across LLM models",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Multiple prompt styles, response comparison, API integration"
    },
    {
        "name": "Few-Shot vs Zero-Shot Benchmark",
        "description": "Compares accuracy of few-shot vs zero-shot prompting on sentiment analysis",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Automated benchmarking, accuracy scoring, tricky test cases"
    },
    {
        "name": "Chain of Thought Prompting",
        "description": "Demonstrates step by step reasoning with CoT prompting",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Math problem solving, step by step reasoning, comparison with normal prompting"
    },
    {
        "name": "RAG Document Q&A",
        "description": "Question answering system using Retrieval Augmented Generation",
        "tech": "Python, Groq API, FAISS, SentenceTransformers",
        "features": "Vector embeddings, semantic search, context-aware answers"
    },
    {
        "name": "Prompt Injection Defense",
        "description": "Detects and blocks malicious prompt injection attacks",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Pattern matching, attack detection, request blocking"
    },
    {
        "name": "HCI Usability Analyzer",
        "description": "Evaluates apps against Nielsen's 10 usability heuristics",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "10 heuristic scoring, issue detection, improvement suggestions"
    },
    {
        "name": "IoT Alert Summarizer",
        "description": "Converts raw IoT sensor data into intelligent alert summaries",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Critical/warning/normal categorization, action recommendations"
    },
    {
        "name": "ReAct Agent with Tools",
        "description": "LLM agent that reasons and uses tools to answer questions",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Calculator, weather, dictionary tools, reasoning loop"
    },
    {
        "name": "Prompt Response Evaluator",
        "description": "Automatically scores LLM responses across 5 quality criteria",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Relevance, accuracy, completeness, clarity, conciseness scoring"
    },
    {
        "name": "Resume Tailor Bot",
        "description": "Rewrites resume bullets to match specific job descriptions",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Keyword injection, bullet rewriting, job description matching"
    },
    {
        "name": "Structured Output Extractor",
        "description": "Extracts structured JSON from unstructured text",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Custom schema extraction, JSON parsing, multiple data types"
    },
    {
        "name": "Multi-Turn Chatbot with Memory",
        "description": "Career coach chatbot that remembers conversation history",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Conversation memory, context awareness, persona prompting"
    },
    {
        "name": "LLM Code Reviewer",
        "description": "Reviews code for bugs, security issues and performance",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Bug detection, SQL injection detection, performance optimization"
    },
    {
        "name": "Persona Prompting Experiment",
        "description": "Tests how different personas affect LLM response style",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "5 different personas, vocabulary analysis, tone comparison"
    },
    {
        "name": "Graph Problem Explainer Bot",
        "description": "Explains graph algorithms with pseudocode and complexity analysis",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Pseudocode generation, complexity analysis, real world examples"
    },
    {
        "name": "Prompt A/B Testing Dashboard",
        "description": "Compares two prompts across multiple test inputs with scoring",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Automated scoring, winner selection, data-driven comparison"
    },
    {
        "name": "LLM API Rate Limiter",
        "description": "Handles high volume API requests with rate limiting and retry",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Rate limiting, exponential backoff, queue management"
    },
    {
        "name": "Multimodal Prompting Demo",
        "description": "Analyzes images with text questions using vision LLM",
        "tech": "Python, Groq API, LLaMA 4 Scout Vision",
        "features": "Image analysis, base64 encoding, visual Q&A"
    },
    {
        "name": "Fine-Tuning Data Prep Pipeline",
        "description": "Generates JSONL training data for LLM fine-tuning",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Q&A generation, JSONL formatting, multiple topics"
    },
    {
        "name": "Portfolio README Generator",
        "description": "Automatically generates professional READMEs for all projects",
        "tech": "Python, Groq API, LLaMA 3.1",
        "features": "Batch README generation, professional formatting, recruiter-ready"
    },
]

print("📝 Portfolio README Generator")
print("=" * 60)
print(f"Generating READMEs for {len(projects)} projects...\n")

for i, project in enumerate(projects):
    print(f"🔨 Generating README for: {project['name']}")
    
    readme = generate_readme(
        project["name"],
        project["description"],
        project["tech"],
        project["features"]
    )
    
    filename = f"README_project{i+1}.md"
    save_readme(readme, filename)
    print(f"📄 Preview: {readme[:150]}...\n")

print("=" * 60)
print(f"✅ Generated {len(projects)} READMEs!")
print("📁 Check the generated README files in this folder!")