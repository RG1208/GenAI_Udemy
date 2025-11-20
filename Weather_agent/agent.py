# a prompting technique where we directly give the instructions to the model and some examples of the task we want it to perform 
#  used more
from openai import OpenAI #type:ignore
from dotenv import load_dotenv #type:ignore
import json
import requests #type:ignore

load_dotenv()

client = OpenAI(
    api_key="AIzaSyBuXAlcUk2r2b4flWZohNaMiSTBVaR2sW0",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    headers = {"User-Agent": "Mozilla/5.0"}  # Pretend like a browser
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return f"the weather in {city} is {response.text.strip()}"
    else:
        return f"Sorry, couldn't fetch weather (status {response.status_code})."

SYSTEM_PROMPT = """
    you are an expert AI assistant which helps users in their queries using chain of thought process.
    you work on START, PLAN and OUTPUT strategy.
    you need to plan what needs to be done. the plan can be multiple steps.
    once you think enough plan has been done, you will output the final answer OUTPUT.
    you can also call a tool from the available tools if needed.

    Rules:
    - strictly follow JSON format.
    - only run one step at a time.
    - the sequence of steps is START(where the user gives the input), 
    PLAN(where you plan what needs to be done and can be run multiple times) and  
    OUTPUT(where you give the final answer and displayed to the user).

    Tools:
    get_weather(city: str)  : get the city name and fetches the current weather of the city.
    Output JSON Format:
    {
        "step": "START" or "PLAN" or "OUTPUT" or "TOOl" "tool":"string", "input":"string",
        "content": "string" 
    }

    Example 1:
    {"step": "START", "content": "can you solve 2+3*4/10?"}
    {"step": "PLAN", "content": "I think the user is intrested in solving a maths problem."}
    {"step": "PLAN", "content": "This can be solved using BODMAS rule."}
    {"step": "PLAN", "content": "I will first solve 3*4=12,"}
    {"step": "PLAN", "content": "then I will solve 12/10=1.2 "}
    {"step": "PLAN", "content": "and finally I will solve 2+1.2=3.2"}
    {"step": "OUTPUT", "content": "the final ans er is 3.2}

    Example 2:
    {"step": "START", "content": "what is the weather in New York?"
    {"step": "PLAN", "content": "I think the user is intrested in knowing the weather of New York."}
    {"step": "PLAN", "content": "I will use the tool get_weather to get the current weather of New York."}
    {"step": "TOOL", "content": "get_weather('New York')"}
    {"step": "PLAN", "content": "I have got the weather information from the tool."}
    {"step": "OUTPUT", "content": "the weather in New York is 25C and sunny."}

"""
message_history = [
    {"role":  "system", "content": SYSTEM_PROMPT},
]

user_query= input("👉🏻 Enter your query: ")
message_history.append({"role":  "user", "content": user_query})

while True:

    response=client.chat.completions.create(
        model="gemini-2.5-flash", 
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = (response.choices[0].message.content)
    message_history.append({"role":  "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result['step'] == "STARTS":
        print("🔥: Starting the chain of thought process...", parsed_result.get("content"))
        continue

    if parsed_result['step'] == "TOOL":

    if parsed_result['step'] == "PLAN":
        print("🧠: Planning...", parsed_result.get("content"))
        continue
    
    if parsed_result['step'] == "OUTPUT":
        print("🤖: Final Output:", parsed_result.get("content"))
        break

