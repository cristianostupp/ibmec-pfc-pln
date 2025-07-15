from anyio import sleep
from decodificador_de_normas import Decodificador
from ocr import OCR
from ingestor import Ingestor
from db_vetorial import DBVetorial

caminho_do_arquivo = 'files/cct-siescomet-2024-2025_ocr.txt'

decodificador = Decodificador(caminho_do_arquivo)

# Se o arquivo a ser processado não for texto digital,
# ou seja, se for escaneado, então realiza OCR
if not decodificador.eh_arquivo_texto_digital():
    ocr = OCR(caminho_do_arquivo)
    ocr.carregar_paginas()
    ocr.extrair_texto()
    decodificador.caminho_do_arquivo = ocr.salvar_txt()

# Pré-processa (limpa, separa cláusulas e gera chunks)
decodificador.pre_processar()

# Gera embeddings e armazena no banco vetorial
ingestor = Ingestor()
ingestor.processar_chunks(decodificador.chunks)

# ...
print("\n--- Verificação pós-ingestão ---")
db_verificacao = DBVetorial() # Esta linha é crucial para verificar se está lendo do disco
print(f"DEBUG: Total de documentos na coleção 'acordos' APÓS EXECUÇÃO DE MAIN.PY: {db_verificacao.collection.count()}")
print("--------------------------------\n")
sleep(10)  # Aguarda 1 segundo para garantir que a saída seja limpa antes de imprimir
# ...

#print(decodificador.clausulas)
#print(decodificador.chunks)

print("📦 Total de chunks inseridos:", len(ingestor.db.collection.get()["documents"]))

for doc in ingestor.db.collection.get()["documents"][:3]:
    print("\n📄", doc[:300])
