import chromadb
from pprint import pprint


client = chromadb.PersistentClient(path="../db")

collection = client.get_collection("support_faqs")

data = collection.get()

pprint(data)