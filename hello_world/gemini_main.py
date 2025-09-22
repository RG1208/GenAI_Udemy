from google import genai

client = genai.Client(
    api_key="AIzaSyBuXAlcUk2r2b4flWZohNaMiSTBVaR2sW0"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents= "Hello there!"
) 

print(response.text)