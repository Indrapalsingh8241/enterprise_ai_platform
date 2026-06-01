from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from .embeddings import embeddings

documents = []

files = [
    "RAG/documents/business_insights.txt",
    "RAG/documents/model_results.txt",
    "RAG/documents/feature_importance.txt",
    "RAG/documents/recommendations.txt"
]

for file in files:
    loader = TextLoader(file)
    documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="RAG/chroma_db"
)


print(f"Chunks created: {len(chunks)}")