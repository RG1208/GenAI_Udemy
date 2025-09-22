# a prompting technique where the model is told directly what to do
from openai import OpenAI #type:ignore
from dotenv import load_dotenv #type:ignore

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBuXAlcUk2r2b4flWZohNaMiSTBVaR2sW0",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":  "system", "content": "you are a maths expert and only and only required to answer maths questions if any other question is asked you will reply with I am a maths expert"},
        {"role":  "user", "content": "what is 2+2"}
    ]
)

print(response.choices[0].message.content)