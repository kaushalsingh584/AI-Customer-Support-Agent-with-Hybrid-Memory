# AI Customer Support Agent

An AI-powered customer support chatbot built using Retrieval-Augmented Generation (RAG), vector embeddings, and local LLMs.

This project allows users to ask customer support questions in natural language. The system retrieves relevant FAQs from a vector database and generates human-like responses.

---

## Features

* FAQ-based customer support chatbot
* Semantic search using vector embeddings
* Vector database integration using Chroma
* Local LLM inference using Ollama
* Hallucination control (answers only from provided context)
* Built with zero paid APIs

---

## Tech Stack

### AI / ML

* Python
* Sentence Transformers
* Ollama

### Vector Database

* Chroma

### Model

* Llama 3

---

## Project Architecture

User Query
↓
Embedding Generation
↓
Semantic Search in Chroma
↓
Relevant FAQ Retrieval
↓
Response Generation using LLM

---

## Project Structure

```bash
ai-support-agent/
│
├── data/
│   └── faq.json
│
├── db/
│
├── src/
│   ├── ingest.py
│   ├── chatbot.py
│   └── view_db.py
│
├── venv/
│
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/kaushalsingh584/AI-Customer-Support-Agent-with-Hybrid-Memory.git
cd ai-support-agent
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install chromadb sentence-transformers requests
```

---

### 4. Install Ollama

Install Ollama and pull the model:

```bash
ollama pull llama3
```

---

### 5. Prepare FAQ data

Add FAQ data inside:

```bash
data/faq.json
```

Example:

```json
[
  {
    "question": "What is your refund policy?",
    "answer": "Refunds are available within 7 days."
  }
]
```

---

### 6. Build knowledge base

```bash
cd src
python ingest.py
```

This creates vector embeddings and stores them in Chroma.

---

### 7. Run chatbot

Make sure Ollama is running:

```bash
ollama serve
```

Then:

```bash
python chatbot.py
```

---

## Example Queries

Try asking:

* How can I get my money back?
* Where can I track my package?
* How long does delivery take?

---

## Current Progress

### Phase 1: Knowledge Retrieval

* [x] FAQ ingestion
* [x] Embedding generation
* [x] Chroma vector database integration
* [x] LLM response generation

### Phase 2: Conversation Memory

* [ ] In progress

---

## Future Enhancements

* Conversation memory
* Long-term user memory
* Tool calling (Order tracking, Refund APIs)
* Human escalation workflow

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector embeddings
* Semantic search
* Vector databases
* Local LLM deployment
