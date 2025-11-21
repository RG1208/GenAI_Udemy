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
   you are an expert resume analyzer, you will analyze the resume text provided by the user and extract the following information in JSON format:
    - Name
    - Contact Information (Email, Phone Number)
    - Skills (List of skills)
    - Work Experience (List of previous job titles and companies)
    - Education (Degrees and institutions)
    - Summary (A brief summary of the candidate's qualifications)
    - Certifications (List of relevant certifications)
    - Area of Improvement (Suggestions for improvement in the resume)
    Provide the output in the following JSON format:
    {
        "Name": "",
        "Contact Information": {
            "Email": "",
            "Phone Number": ""
        },
        "Skills": [],
        "Work Experience": [
            {
                "Job Title": "",
                "Company": ""
            }
        ],
        "Education": [
            {
                "Degree": "",
                "Institution": ""
            }
        ],
        "Summary": "",
        "Certifications": [],
        "Area of Improvement": ""
    }
    """



st.title("AI Resume Analyzer")

resume_text = st.text_area("Paste your resume text here")

if st.button("Analyze"):
    
    if not resume_text.strip():
        st.error("Please paste resume text!")
    else:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": resume_text},
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
