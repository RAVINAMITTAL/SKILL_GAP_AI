from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load PDF
loader = PyPDFLoader("data/resume.pdf")
docs = loader.load()

print("Pages Loaded:", len(docs))

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)

print("\nTotal Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content)
# Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding Model Loaded")
# Create Vector DB

vectorstore = FAISS.from_documents(
    chunks,
    embedding_model
)

# Save DB

vectorstore.save_local("vectorstore")

print("FAISS Database Created Successfully")