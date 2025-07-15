from dotenv import load_dotenv
import os
from openai import OpenAI
import httpx

load_dotenv()

class GeradorDeEmbedding:
    def __init__(self, model="text-embedding-3-small"):
        self.model = model
        # Cria um cliente httpx que não verifica o SSL
        # CUIDADO: Desabilita a verificação de segurança. Use com cautela!
        http_client = httpx.Client(verify=False) 
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], http_client=http_client)

    def gerar(self, texto: str):
        response = self.client.embeddings.create(
            input=texto,
            model=self.model
        )
        return response.data[0].embedding
