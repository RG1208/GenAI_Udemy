from openai import OpenAI #type:ignore
from dotenv import load_dotenv #type:ignore

load_dotenv()

client = OpenAI()

response=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":  "user", "content": "Hey there!"}
    ]
)

print(response.choices[0].message.content)