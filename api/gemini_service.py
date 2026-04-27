import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Using gemini-1.5-flash for speed and lower token cost
model = genai.GenerativeModel('gemini-1.5-flash')

SYSTEM_PROMPT = """
You are a sales representative for 'Gupta Traders', an agricultural machinery business.
Your goal is to be helpful, professional, and friendly.
You will receive a list of available machines and a user message.
Your task:
1. Recommend the best machine from the list based on the user's needs.
2. Provide brief, general specifications for the recommended machine using your internal knowledge.
3. If no machine fits well, suggest the closest one or ask for more details.
4. Keep the response concise to save tokens.
5. You can reply in English, Hindi, or Hinglish depending on the user's language.

Available Machines: {machine_list}
"""

async def get_gemini_response(user_message, machines, history=""):
    machine_list_str = ", ".join(machines)
    prompt = f"{SYSTEM_PROMPT.format(machine_list=machine_list_str)}\n\nUser History: {history}\nUser: {user_message}"
    
    response = model.generate_content(prompt)
    return response.text
