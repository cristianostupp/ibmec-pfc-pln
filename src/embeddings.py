from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

class GeradorDeEmbedding:
    def __init__(self, model="text-embedding-3-small"):
        self.model = model
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def gerar(self, texto: str):
        response = self.client.embeddings.create(
            input=texto,
            model=self.model
        )
        return response.data[0].embedding
