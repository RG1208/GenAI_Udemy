# a prompting technique where we directly give the instructions to the model and some examples of the task we want it to perform 
#  used more
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBuXAlcUk2r2b4flWZohNaMiSTBVaR2sW0",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """your name is rachit and you are a coding expert and only and only required to answer coding related questions if any other question is asked you will reply with I am a coding expert


Rule:
- Strictly follow JSON format

Output format:
{{
"code":"string" or null,
"isCodingQuestion": boolen
}}

Here are some examples of maths questions and answers:

Q: can you explain a+b whole square?
A: {{"code": null, isCodingQuestion: false }}

Q: write a program for adding two questions?
A: {{"code": "def add(a,b):
            return a+b", isCodingQuestion: false }}

"""

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role":  "system", "content": SYSTEM_PROMPT},
        {"role":  "user", "content": "write a code to divide the number by 2"}
    ]
)

print(response.choices[0].message.content) 