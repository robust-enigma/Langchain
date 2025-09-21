# from langchain_openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()

# llm=OpenAI(model='gpt-3.5-turbo-instruct')

# result= llm.invoke("Who is the director of Shrek?")

# print(result)



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
