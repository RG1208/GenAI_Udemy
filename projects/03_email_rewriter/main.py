# Persona Based Prompting
from openai import OpenAI #type:ignore
from dotenv import load_dotenv#type:ignore 
import json
import os
import streamlit as st # type: ignore

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
   you are an expert email rewriter.
   Your task is to analyze the email content provided by the user and rewrite it to be more professional, concise, and clear.
   your tone must be more formal, polite and professional.
   You must:
    - Improve grammar and clarity
    - Use the selected tone
    - Maintain the original meaning
    - Avoid sounding robotic
    - Keep it customer-friendly
   Please provide the rewritten email in the following JSON format:
    {
    "original_tone": "angry",
    "formatted_tone": "professional",
    "formatted_email": "Hi, I ordered a laptop..."
    }
    """


st.title("AI Email Rewriter")

email_content = st.text_area("Paste your email content here")

if st.button("Analyze"):
    
    if not email_content.strip():
        st.error("Please paste email content!")
    else:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": email_content},
            ]
        )

        raw_output = response.choices[0].message.content

        try:
            json_output = json.loads(raw_output)
            st.success("Analysis Successful!")

            st.json(json_output)   # Pretty display
        except:
            st.error("Model did not return valid JSON. Try again.")
            st.write(raw_output)
