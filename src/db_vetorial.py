from anyio import sleep
import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.api.types import EmbeddingFunction
from typing import List

class SentenceTransformerEmbeddingFunction(EmbeddingFunction):
    def __init__(self, model_path: str = "models/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_path)

    def __call__(self, input: List[str]) -> List[List[float]]:
        return self.model.encode(input, convert_to_numpy=True).tolist()


class DBVetorial:
    def __init__(self, collection_name="acordos", persist_dir="./chroma"):
        embedding_fn = SentenceTransformerEmbeddingFunction()

        self.client = chromadb.PersistentClient(path=persist_dir)

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_fn
        )

    def inserir(self, ids, textos, embeddings, metadados):
        self.collection.add(
            documents=textos,
            ids=ids,
            embeddings=embeddings,
            metadatas=metadados
        )
        print(f"DEBUG: Inseridos {len(ids)} documentos na coleção '{self.collection.name}'.")
        print(f"DEBUG: Total de documentos na coleção '{self.collection.name}' APÓS INSERÇÃO: {self.collection.count()}")
        sleep(10)

       
    def buscar(self, consulta, k=3):
        return self.collection.query(
            query_texts=[consulta],
            n_results=k,
            include=['documents', 'distances']
        )
