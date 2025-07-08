from embeddings import GeradorDeEmbedding
from db_vetorial import DBVetorial

class Ingestor:
    def __init__(self):
        self.embedding = GeradorDeEmbedding()
        self.db = DBVetorial()

    def processar_chunks(self, chunks):
        ids = [chunk["id"] for chunk in chunks]
        textos = [chunk["texto"] for chunk in chunks]
        embeddings = [self.embedding.gerar(txt) for txt in textos]
        metadados = [{"origem": "CCT", "tipo": "clausula"} for _ in textos]

        self.db.inserir(ids, textos, embeddings, metadados)
