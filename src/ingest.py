import json
import chromadb
import numpy as np
from sentence_transformers import SentenceTransformer

# Load FAQ data
with open("../data/faq.json", "r") as f:
    faq_data = json.load(f)

# Convert FAQs to searchable text chunks
documents = [
    f"Q: {item['question']} A: {item['answer']}"
    for item in faq_data
]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(documents).tolist()

# Create persistent Chroma DB
client = chromadb.PersistentClient(path="../db")

# Create collection
collection = client.get_or_create_collection(
    name="support_faqs"
)

# Store data
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(documents))]
)

print("Knowledge base created successfully!")