# db_vetorial.py
from chromadb import PersistentClient

class DBVetorial:
    def __init__(self, collection_name="acordos", persist_dir="./chroma"):
        self.client = PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def inserir(self, ids, textos, embeddings, metadados):
        self.collection.add(documents=textos, ids=ids, embeddings=embeddings, metadatas=metadados)

    def buscar(self, consulta, k=3):
        return self.collection.query(query_texts=[consulta], n_results=k)
