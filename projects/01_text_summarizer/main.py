# Persona Based Prompting
from openai import OpenAI #type:ignore
from dotenv import load_dotenv#type:ignore 
import json
import os
import streamlit as st

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    you are an AI Assistant which is best at summarizing long text into 5 bullet points.
    You always respond in a concise manner.
    your main aim is to carefully the long text and extract only the most important information.
    The output must be an ordered list of 5 bullet points.
    """

st.title("AI Text Summarizer")

text = st.text_area("Enter your text")

# user_text = input("\nEnter the text you want to summarize:\n\n")

if st.button("Summarize"):
    response=client.chat.completions.create(
        model="gemini-2.5-flash", 
        messages=[
            {"role":  "system", "content": SYSTEM_PROMPT},
            {"role":  "user", "content": text},
        ]
    )

    st.subheader("Summary")
    st.write(response.choices[0].message.content)