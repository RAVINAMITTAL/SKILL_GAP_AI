from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def ask_resume_question(
    retriever,
    question
):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a professional resume assistant.

Use ONLY the resume context below.

Resume Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content