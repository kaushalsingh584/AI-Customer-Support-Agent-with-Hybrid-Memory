import json
import re
import chromadb
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

from tools import track_order

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Chroma
client = chromadb.PersistentClient(path="../db")

# Load collection
collection = client.get_collection(
    name="support_faqs"
)

chat_history = []

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

    # Tool detection for order tracking
    if "ORD" in user_query.upper():
        words = user_query.split()

    order_id = None

    match = re.search(r'ORD\d+', user_query.upper())

    if match:
        order_id = match.group()
        print("requested order id:"+order_id)
        result = track_order(order_id)

        print(f"\nBot: {result}")

        chat_history.append(f"User: {user_query}")
        chat_history.append(f"Bot: {result}")

        continue
    
    # Store user message
    chat_history.append(f"User: {user_query}")

    # Retrieve FAQ context
    retrieved_docs = search_knowledge_base(user_query)

    faq_context = "\n".join(retrieved_docs)

    # Keep recent conversation only ( last 6 conversations )
    memory_context = "\n".join(chat_history[-6:])

    # Combine FAQ + conversation memory
    full_context = f"""

    FAQ Context:
    {faq_context}

    Conversation History:
    {memory_context}
    """     

    answer = ask_llm(full_context, user_query)

    print("\nBot:", answer)

    # Store bot response
    chat_history.append(f"Bot: {answer}")