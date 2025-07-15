from rag import RAG

rag = RAG(k=3)

pergunta = input("Digite sua pergunta: ")
resposta = rag.responder_pergunta(pergunta)

print("\n💬 Resposta:\n", resposta)
