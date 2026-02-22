import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---- TOOLS ----
def calculator(expression):
    try:
        result = eval(expression)
        return f"Calculator result: {result}"
    except:
        return "Calculator error: invalid expression"

def weather(city):
    # Simulated weather data
    weather_data = {
        "new york": "72°F, Sunny",
        "london": "58°F, Cloudy",
        "tokyo": "65°F, Partly Cloudy",
        "hyderabad": "85°F, Hot",
        "corvallis": "55°F, Rainy",
    }
    return weather_data.get(city.lower(), "Weather data not available")

def dictionary(word):
    definitions = {
        "recursion": "A function that calls itself until a base case is reached",
        "algorithm": "A step-by-step procedure to solve a problem",
        "api": "Application Programming Interface - allows apps to communicate",
    }
    return definitions.get(word.lower(), "Definition not found")

# ---- REACT AGENT ----
TOOLS_DESCRIPTION = """
You have access to these tools:
- calculator(expression): For math calculations e.g. calculator(15 * 847 / 100)
- weather(city): Get weather for a city e.g. weather(New York)
- dictionary(word): Get definition of a word e.g. dictionary(recursion)

To use a tool, respond with:
TOOL: tool_name(input)

If you don't need a tool, respond with:
ANSWER: your answer
"""

def run_agent(question):
    print(f"\n❓ Question: {question}")
    print("-" * 60)
    
    messages = [
        {"role": "system", "content": TOOLS_DESCRIPTION},
        {"role": "user", "content": question}
    ]
    
    # ReAct loop - reason and act up to 3 times
    for i in range(3):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )
        
        reply = response.choices[0].message.content.strip()
        print(f"🧠 Agent thinks: {reply}")
        
        # Check if agent wants to use a tool
        if reply.startswith("TOOL:"):
            tool_call = reply.replace("TOOL:", "").strip()
            
            # Execute the right tool
            if tool_call.startswith("calculator"):
                expr = tool_call.replace("calculator(", "").rstrip(")")
                result = calculator(expr)
            elif tool_call.startswith("weather"):
                city = tool_call.replace("weather(", "").rstrip(")")
                result = weather(city)
            elif tool_call.startswith("dictionary"):
                word = tool_call.replace("dictionary(", "").rstrip(")")
                result = dictionary(word)
            else:
                result = "Unknown tool"
            
            print(f"🔧 Tool result: {result}")
            
            # Feed result back to agent
            messages.append({"role": "assistant", "content": reply})
            messages.append({"role": "user", "content": f"Tool result: {result}. Now answer the question."})
        
        elif reply.startswith("ANSWER:"):
            print(f"✅ Final Answer: {reply.replace('ANSWER:', '').strip()}")
            break

# Test the agent
run_agent("What is 15% of 847?")
run_agent("What is the weather in New York?")
run_agent("What does the word recursion mean?")
run_agent("What is the weather in London and convert the temperature to Celsius?")