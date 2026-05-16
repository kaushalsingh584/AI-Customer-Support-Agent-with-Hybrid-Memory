# AI Customer Support Agent

An AI-powered customer support agent built using Retrieval-Augmented Generation (RAG), vector embeddings, tool calling, and persistent memory.

This project allows users to ask customer support questions in natural language. The system retrieves relevant FAQs from a vector database, performs business actions using tools, and remembers previous conversations across sessions.

---

## Features

* FAQ-based customer support chatbot
* Semantic search using vector embeddings
* Vector database integration using Chroma
* Local LLM inference using Ollama
* Hallucination control (answers only from provided context)
* Order tracking tool
* Refund eligibility checking
* Support ticket creation
* Persistent cross-session memory
* Built with zero paid APIs

---

## Tech Stack

### AI / ML

* Python
* Sentence Transformers
* Ollama

### Vector Database

* Chroma

### Business Database

* SQLite

### Model

* Llama 3

---

## Project Architecture

User Query  
↓  
Intent Detection  
↓  
Route to Tool OR Knowledge Base  
↓  

If FAQ Query:

Embedding Generation  
↓  
Semantic Search in Chroma  
↓  
Relevant FAQ Retrieval  
↓  
Response Generation using LLM  

If Action Query:

Tool Execution (SQLite)  
↓  
Business Response Returned  

---

## Project Structure

```bash
ai-support-agent/
│
├── data/
│   ├── faq.json
│   └── orders.db
│
├── db/
│
├── src/
│   ├── ingest.py
│   ├── chatbot.py
│   ├── tools.py
│   ├── create_orders_db.py
│   └── view_db.py
│
├── venv/
│
├── requirements.txt
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
pip install -r requirements.txt
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

### 6. Create business database

```bash
cd src
python create_orders_db.py
```

This creates:

* Orders table
* Tickets table
* Memory table

---

### 7. Build knowledge base

```bash
python ingest.py
```

This creates vector embeddings and stores them in Chroma.

---

### 8. Run chatbot

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

### FAQ Retrieval

* What is your refund policy?
* How long does delivery take?

### Order Tracking

* Track my order ORD123
* Where is ORD456?

### Refund Check

* Can I get a refund for ORD123?

### Ticket Creation

* I want to talk to a human
* My product is damaged

### Persistent Memory

* What issue did I report earlier?
* What happened with my order?

---

## Current Progress

### Phase 1: Knowledge Retrieval

* [x] FAQ ingestion
* [x] Embedding generation
* [x] Chroma vector database integration
* [x] LLM response generation

### Phase 2: Conversation Memory

* [x] Session memory

### Phase 3: Tool Calling

* [x] Order tracking
* [x] Refund eligibility
* [x] Ticket creation

### Phase 4: Persistent Memory

* [x] Cross-session memory using SQLite

---

## Future Enhancements

* Multi-agent architecture
* User authentication
* Web UI
* Real order APIs
* Analytics dashboard

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector embeddings
* Semantic search
* Vector databases
* Tool calling
* Persistent memory systems
* Local LLM deployment
* AI agent architecture