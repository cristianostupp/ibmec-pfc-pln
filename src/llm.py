import ollama

class LLM:
    def __init__(self, model="llama3"):
        self.model = model

    def responder(self, prompt: str):
        resposta = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": "Você é um assistente jurídico especializado em Acordos Coletivos de Trabalho."},
                {"role": "user", "content": prompt}
            ]
        )
        return resposta["message"]["content"].strip()
