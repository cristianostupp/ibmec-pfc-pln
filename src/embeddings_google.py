# embeddings.py
from dotenv import load_dotenv
import os
import google.generativeai as genai
import httpx

load_dotenv()

class GeradorDeEmbedding:
    def __init__(self, model="models/embedding-001"):
        self.model = model
        
        # CUIDADO: Desabilita a verificação de segurança da conexão SSL.
        # Use APENAS para desenvolvimento e testes em ambientes controlados.
        # NUNCA use em produção sem uma solução de segurança adequada.
        http_client = httpx.Client(verify=False) 
        
        # O SDK do Google AI permite passar um cliente HTTP customizado
        # via client_options, que deve ser um objeto configure_transport.
        # A forma mais simples de usar httpx com verify=False é assim:
        genai.configure(
            api_key=os.environ["GOOGLE_API_KEY"],
            transport="rest", # Força o uso do transporte REST que usa httpx
            client_options={"http_client": http_client}
        )

    def gerar(self, texto: str):
        response = genai.embed_content(
            model=self.model,
            content=texto
        )
        return response['embedding']