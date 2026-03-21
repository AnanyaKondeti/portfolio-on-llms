import os
import base64
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_local_image(image_path, question):
    try:
        with open(image_path, "rb") as f:
            base64_image = base64.b64encode(f.read()).decode('utf-8')
        
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        },
                        {
                            "type": "text",
                            "text": question
                        }
                    ]
                }
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"

questions = [
    "What do you see in this image?",
    "Describe the colors present",
    "What is the mood or atmosphere of this image?",
]

print("🖼️ Multimodal Prompting Demo")
print("=" * 60)

for question in questions:
    print(f"\n❓ Question: {question}")
    response = analyze_local_image("test.jpg", question)
    print(f"🤖 Answer: {response}")