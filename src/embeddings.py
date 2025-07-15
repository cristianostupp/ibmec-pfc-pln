from sentence_transformers import SentenceTransformer

class GeradorDeEmbedding:
    def __init__(self, modelo="models/all-MiniLM-L6-v2"):
        self.modelo = SentenceTransformer(modelo)

    def gerar(self, texto: str):
        return self.modelo.encode(texto, convert_to_numpy=True).tolist()
