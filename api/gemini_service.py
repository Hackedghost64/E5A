import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Using gemini-2.5-flash for the latest stable speed and lowest token cost
model = genai.GenerativeModel('gemini-2.5-flash')

SYSTEM_PROMPT = """
You are a sales representative for 'Gupta Traders', an agricultural machinery business.
Your goal is to be helpful, professional, and friendly.

RULES:
1. Identify the user's need from their message.
2. Recommend the best machine from the provided 'Available Machines' list.
3. Provide brief, general specifications (HP, capacity, or durability) based on your internal knowledge.
4. Language: If the user speaks Hindi, reply in Hindi. If they use Hinglish, reply in Hinglish.
5. Tone: Keep it concise but persuasive.
6. If they ask for something not in the list, politely tell them we don't have it but suggest the closest alternative.

Available Machines: {machine_list}
"""

async def get_gemini_response(user_message, machines, history=""):
    if not os.getenv("GEMINI_API_KEY") or "your_google" in os.getenv("GEMINI_API_KEY"):
        return "Error: Gemini API Key not configured correctly."

    machine_list_str = ", ".join(machines)
    prompt = f"{SYSTEM_PROMPT.format(machine_list=machine_list_str)}\n\nUser History: {history}\nUser: {user_message}"
    
    response = model.generate_content(prompt)
    return response.text
