import json
import faiss
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
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(np.array(embeddings).astype("float32"))

# Save index
faiss.write_index(index, "../data/faiss_index.bin")

# Save documents separately
with open("../data/documents.json", "w") as f:
    json.dump(documents, f)

print("Knowledge base created successfully!")