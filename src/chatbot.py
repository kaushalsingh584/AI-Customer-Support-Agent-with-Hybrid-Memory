import json
import chromadb
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Chroma
client = chromadb.PersistentClient(path="../db")

# Load collection
collection = client.get_collection(
    name="support_faqs"
)


def search_knowledge_base(query, top_k=2):
    # Convert query into vector
    query_embedding = model.encode([query]).tolist()

    # Search Chroma
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results["documents"][0]


def ask_llm(context, question):
    prompt = f"""
You are a customer support assistant.

Answer ONLY using the context below.
If the answer is not found, say:
"I don't have that information."

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


while True:
    user_query = input("\nYou: ")

    if user_query.lower() in ["exit", "quit"]:
        break

    retrieved_docs = search_knowledge_base(user_query)

    context = "\n".join(retrieved_docs)

    answer = ask_llm(context, user_query)

    print("\nBot:", answer)