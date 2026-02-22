import os
from groq import Groq
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
model = SentenceTransformer('all-MiniLM-L6-v2')

# Our "document" - imagine this is a company policy PDF
documents = [
    "Employees get 15 days of paid leave per year.",
    "Remote work is allowed up to 3 days per week.",
    "Health insurance covers employee and immediate family.",
    "Performance reviews happen every 6 months.",
    "Travel expenses must be submitted within 30 days.",
    "Office hours are 9am to 6pm Monday to Friday.",
]

# Step 1: Convert documents to vectors
print("📚 Loading documents...")
embeddings = model.encode(documents)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))
print(f"✅ Loaded {len(documents)} documents\n")

def ask(question):
    # Step 2: Find relevant documents
    question_embedding = model.encode([question])
    distances, indices = index.search(np.array(question_embedding), k=2)
    relevant_docs = [documents[i] for i in indices[0]]
    context = "\n".join(relevant_docs)
    
    # Step 3: Answer using context
    prompt = f"""Answer the question using ONLY the context below.
Context: {context}
Question: {question}
Answer:"""
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    
    print(f"❓ Question: {question}")
    print(f"📄 Relevant docs found: {relevant_docs}")
    print(f"🤖 Answer: {response.choices[0].message.content.strip()}")
    print("-" * 60)

ask("How many leave days do I get?")
ask("Can I work from home?")
ask("When are performance reviews?")