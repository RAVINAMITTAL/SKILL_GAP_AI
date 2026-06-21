from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS
db = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever()

# User question
query = "What skills does this candidate have?"

# Retrieve context
docs = retriever.invoke(query)

context = "\n\n".join(
    [doc.page_content for doc in docs]
)

# Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are a professional resume analyzer.

Use ONLY the resume context below.

Resume Context:
{context}

Question:
{question}
""")

final_prompt = prompt.invoke({
    "context": context,
    "question": query
})

response = llm.invoke(final_prompt)

print(response.content)