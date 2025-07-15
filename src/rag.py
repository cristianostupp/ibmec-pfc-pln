from embeddings import GeradorDeEmbedding
from db_vetorial import DBVetorial
from llm import LLM

class RAG:
    def __init__(self, k=3):
        self.embedding = GeradorDeEmbedding()
        self.vetor_db = DBVetorial()
        self.llm = LLM()
        self.k = k

    def responder_pergunta(self, pergunta: str):
        emb = self.embedding.gerar(pergunta)
        resultados = self.vetor_db.collection.query(
            query_embeddings=[emb],
            n_results=self.k,
            include=["documents"]
        )
        chunks = resultados["documents"][0]
        contexto = "\n\n".join(chunks)

        prompt = (
            f"Baseando-se no seguinte conteúdo extraído de Acordos Coletivos de Trabalho:\n\n"
            f"{contexto}\n\n"
            f"Responda de forma clara e objetiva à seguinte pergunta:\n{pergunta}"
        )

        return self.llm.responder(prompt)
