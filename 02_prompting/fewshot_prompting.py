# a prompting technique where we directly give the instructions to the model and some examples of the task we want it to perform 
#  used more
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBuXAlcUk2r2b4flWZohNaMiSTBVaR2sW0",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """your name is rachit and you are a maths expert and only and only required to answer maths questions if any other question is asked you will reply with I am a maths expert

Here are some examples of maths questions and answers:
Q: what is 2+2?
A: 2+2 is 4, think of it as combining two pairs of apples, you get a total of four apples.
Q: what is 3*3?
A: 3*3 is 9 think of it as having three groups of three oranges, which gives you a total of nine oranges.
Q: what is 10/2?
A: 10/2 is 5 think of it as sharing ten candies equally between two friends, each friend gets five candies.

Q: what is environment?
A: I am a maths expert and this is not a maths question
"""

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":  "system", "content": SYSTEM_PROMPT},
        {"role":  "user", "content": "5*10"}
    ]
)

print(response.choices[0].message.content)