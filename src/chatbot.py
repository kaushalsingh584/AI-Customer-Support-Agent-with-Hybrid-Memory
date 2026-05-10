import chromadb
import requests
import re
from sentence_transformers import SentenceTransformer

from tools import track_order, check_refund


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Connect to Chroma DB
client = chromadb.PersistentClient(path="../db")

collection = client.get_collection(
    name="support_faqs"
)


# Short-term conversation memory
chat_history = []


def search_knowledge_base(query, top_k=2):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results["documents"][0]


def ask_llm(context, question):
    prompt = f"""
You are a customer support assistant.

Rules:
1. Use FAQ context first.
2. Use conversation history to understand follow-up questions.
3. If answer is not found, say:
"I don't have that information."

Context:
{context}

Current Question:
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

    # Save user message
    chat_history.append(f"User: {user_query}")

    # --------------------------
    # Refund tool
    # --------------------------
    if "refund" in user_query.lower():

        match = re.search(
            r'ORD\d+',
            user_query.upper()
        )

        if match:
            order_id = match.group()

            result = check_refund(
                order_id
            )

            print(
                f"\nBot: {result}"
            )

            chat_history.append(
                f"Bot: {result}"
            )

            continue

    # --------------------------
    # Order tracking tool
    # --------------------------
    match = re.search(
        r'ORD\d+',
        user_query.upper()
    )

    if match:
        order_id = match.group()

        result = track_order(
            order_id
        )

        print(
            f"\nBot: {result}"
        )

        chat_history.append(
            f"Bot: {result}"
        )

        continue

    # --------------------------
    # FAQ Retrieval + Memory
    # --------------------------
    retrieved_docs = search_knowledge_base(
        user_query
    )

    faq_context = "\n".join(
        retrieved_docs
    )

    # Keep recent memory only
    memory_context = "\n".join(
        chat_history[-6:]
    )

    # Combine FAQ + memory
    full_context = f"""
FAQ Context:
{faq_context}

Conversation History:
{memory_context}
"""

    answer = ask_llm(
        full_context,
        user_query
    )

    print(
        f"\nBot: {answer}"
    )

    # Save bot response
    chat_history.append(
        f"Bot: {answer}"
    )