# from dotenv import load_dotenv
# import os

# load_dotenv()

# print(os.getenv("GOOGLE_API_KEY"))
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

response = llm.invoke(
    "What is DBMS?"
)

print(response.content)
# connect internally by the langchain
