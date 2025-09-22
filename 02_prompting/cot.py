# a prompting technique where we directly give the instructions to the model and some examples of the task we want it to perform 
#  used more
from openai import OpenAI #type:ignore
from dotenv import load_dotenv#type:ignore 
import json

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBuXAlcUk2r2b4flWZohNaMiSTBVaR2sW0",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    you are an expert AI assistant which helps users in their queries using chain of thought process.
    you work on START, PLAN and OUTPUT strategy.
    you need to plan what needs to be done. the plan can be multiple steps.
    once you think enough plan has been done, you will output the final answer OUTPUT.

    Rules:
    - strictly follow JSON format.
    - only run one step at a time.
    - the sequence of steps is START(where the user gives the input), 
    PLAN(where you plan what needs to be done and can be run multiple times) and  
    OUTPUT(where you give the final answer and displayed to the user).

    Output JSON Format:
    {
        "step": "START" or "PLAN" or "OUTPUT",
        "content": "string" 
    }

    Examples:
    {"step": "START", "content": "can you solve 2+3*4/10?"}
    {"step": "PLAN", "content": "I think the user is intrested in solving a maths problem."}
    {"step": "PLAN", "content": "This can be solved using BODMAS rule."}
    {"step": "PLAN", "content": "I will first solve 3*4=12,"}
    {"step": "PLAN", "content": "then I will solve 12/10=1.2 "}
    {"step": "PLAN", "content": "and finally I will solve 2+1.2=3.2"}
    {"step": "OUTPUT", "content": "the final ans er is 3.2}

"""

response=client.chat.completions.create(
    model="gemini-2.5-flash", 
    response_format={"type": "json_object"},
    messages=[
        {"role":  "system", "content": SYSTEM_PROMPT},
        {"role":  "user", "content": "write a code to add n numbers in js"},
        {"role":  "assistant", "content": json.dumps({"step": "START", "content": "write a code to add n numbers in js"})},
        {"role":  "assistant", "content": json.dumps({"step": "PLAN", "content": "The user wants a JavaScript function to add an arbitrary number of inputs. I will define a function that accepts multiple arguments (n numbers) and uses a loop or array method to sum them up. I will consider using rest parameters to handle 'n' numbers easily."})},
        {"role":  "assistant", "content": json.dumps({"step": "PLAN", "content": "I will create a JavaScript function that uses rest parameters (`...numbers`) to accept an arbitrary number of arguments. Inside the function, I will use the `reduce` array method to sum all the numbers. Finally, I will provide the full JavaScript code including an example of how to use it."})},
    ]
)

print(response.choices[0].message.content) 