import os
from groq import Groq
from dotenv import load_dotenv
import random

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Simulated IoT sensor data
def generate_sensor_data():
    return [
        {"sensor": "temperature_node_3", "value": 89.2, "unit": "°C", "threshold": 75},
        {"sensor": "battery_node_7", "value": 4.1, "unit": "%", "threshold": 10},
        {"sensor": "cpu_usage", "value": 98.3, "unit": "%", "threshold": 85},
        {"sensor": "network_node_2", "value": 0, "unit": "connected", "threshold": 1},
        {"sensor": "motion_sensor_1", "value": 1, "unit": "detected", "threshold": 1},
        {"sensor": "memory_usage", "value": 45.2, "unit": "%", "threshold": 90},
        {"sensor": "door_sensor", "value": 1, "unit": "open", "threshold": 0},
        {"sensor": "humidity_node_1", "value": 32.1, "unit": "%", "threshold": 30},
    ]

def summarize_alerts(sensor_data):
    data_str = "\n".join([
        f"- {d['sensor']}: {d['value']}{d['unit']} (threshold: {d['threshold']}{d['unit']})"
        for d in sensor_data
    ])
    
    prompt = f"""You are an IoT system monitor. Analyze these sensor readings and create a clear alert summary.

Sensor Data:
{data_str}

Categorize into:
🚨 CRITICAL: values that exceed threshold and need immediate action
⚠️ WARNING: values approaching threshold
✅ NORMAL: values within safe range

For each alert explain WHY it's critical and WHAT action to take."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Run the summarizer
print("🔍 IoT Alert Summarizer")
print("=" * 60)
sensor_data = generate_sensor_data()
print("📡 Raw Sensor Data:")
for d in sensor_data:
    print(f"  {d['sensor']}: {d['value']}{d['unit']}")
print("\n" + "=" * 60)
print("🤖 AI Alert Summary:\n")
print(summarize_alerts(sensor_data))