import json
import faiss
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("../data/faiss_index.bin")

# Load stored documents
with open("../data/documents.json", "r") as f:
    documents = json.load(f)


def search_knowledge_base(query, top_k=2):
    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    results = [documents[i] for i in indices[0]]
    return results


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