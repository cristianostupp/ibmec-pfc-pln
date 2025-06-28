from decodificador_de_normas import Decodificador
from ocr import OCR

caminho_do_arquivo = 'files/CCT-Siescomet-2024-2025-4-9_ocr.txt'

decodificador = Decodificador(caminho_do_arquivo)

# Se o arquivo a ser processado não for texto digital,
# ou seja, se for escaneado, então realiza OCR
if not decodificador.eh_arquivo_texto_digital():
    ocr = OCR(caminho_do_arquivo)
    ocr.carregar_paginas()
    ocr.extrair_texto()
    decodificador.caminho_do_arquivo = ocr.salvar_txt()
    
decodificador.pre_processar()

print(decodificador.clausulas)
print(decodificador.chunks)
