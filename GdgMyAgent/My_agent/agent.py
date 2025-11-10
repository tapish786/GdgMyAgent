from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get the API key
api_key = os.getenv("GOOGLE_API_KEY")

print("API key loaded successfully ✅")

# Example check
if not api_key:
    print("❌ Error: API key not found! Check your .env file.")
else:
    print("🔑 API Key:", api_key[:10] + "********")

from google.adk.agents.llm_agent import Agent

# simple mock tool example - returns a current time string for a city
def get_current_time(city: str) -> dict:
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Tells the current time in a specified city.",
    instruction="You are an assistant that tells the current time in a requested city.",
    tools=[get_current_time],  # register the tool
)
