

from .embeddings import embeddings



from langchain_community.vectorstores import Chroma

db = Chroma(
    persist_directory="RAG/chroma_db",
    embedding_function=embeddings
)


retriever = db.as_retriever(
    search_kwargs={"k": 3}
)
