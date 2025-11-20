from openai import OpenAI #type:ignore
from dotenv import load_dotenv #type:ignore
import requests #type:ignore

load_dotenv()
client = OpenAI()

def get_weather(city: str):
    url = f"http://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"the weather in {city} is {response.text}"
    else:
        return "Sorry, I couldn't fetch the weather information right now."

def main():
    user_query = input(">")
    response=client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":  "user", "content": user_query}
        ]
    )
    print(f"🤖: {response.choices[0].message.content}")

print(get_weather("New York"))