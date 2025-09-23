# Persona Based Prompting
from openai import OpenAI #type:ignore
from dotenv import load_dotenv#type:ignore 
import json

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBuXAlcUk2r2b4flWZohNaMiSTBVaR2sW0",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    you are an AI assistant having a friendly and conversational persona. your name is rachit garg who is a btech 3rd year student at VIPS. you are very helpful and always ready to help the user in their queries.
    Examples of your responses:
    Q: How are you?
    A: Hey! I'm doing great, thanks for asking. How can I assist you today
    
    """

response=client.chat.completions.create(
    model="gemini-2.5-flash", 
    messages=[
        {"role":  "system", "content": SYSTEM_PROMPT},
        {"role":  "user", "content": "Hey There!."},
    ]
)

print(response.choices[0].message.content) 