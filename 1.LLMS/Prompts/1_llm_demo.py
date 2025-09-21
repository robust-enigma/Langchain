# from langchain_openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()

# llm=OpenAI(model='gpt-3.5-turbo-instruct')

# result= llm.invoke("Who is the director of Shrek?")

# print(result)


# from google import genai

# client = genai.Client(api_key="AIzaSyA-TA7A-9XqD17P_n2ExWG0t2vHARx3avg")
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Who is the director of Shrek?"
# )
# print(response.text)

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load variables from .env
load_dotenv()

# Read API key from environment
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM with LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",    # you can also try "gemini-1.5-pro"
    google_api_key=api_key
)

# Ask Gemini something
result = llm.invoke("Who is the director of Shrek?")

print(result.content)
