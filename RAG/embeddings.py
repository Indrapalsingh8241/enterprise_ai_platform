from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
)