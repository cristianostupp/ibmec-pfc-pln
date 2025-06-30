import fitz     # PyMuPDF
import os
import re

class Decodificador:

    def __init__(self, caminho_do_arquivo):
        self.caminho_do_arquivo = caminho_do_arquivo
        self.clausulas = []
        self.chunks = []


    def eh_arquivo_texto_digital(self, paginas_para_testar=2):
        """
        Verifica se o PDF contém texto digital ou se é um PDF escaneado (com imagens).
        :param caminho_do_arquivo: Caminho para o arquivo PDF
        :param paginas_para_testar: Quantas páginas testar antes de concluir
        :return: True se for digital, False se precisar de OCR
        """
        with fitz.open(self.caminho_do_arquivo) as doc:
            for i in range(min(paginas_para_testar, len(doc))):
                texto = doc[i].get_text().strip()
                if len(texto) > 30:  # Considera texto presente se houver conteúdo significativo
                    return True
        return False

    def pre_processar(self):
        texto_completo = self.carregar_texto()
        texto_limpo = self.limpar_texto(texto_completo)
        self.clausulas = self.separar_clausulas(texto_limpo)
        self.chunks = self.gerar_chunks_para_todas_clausulas()
        

    def carregar_texto(self):
        extensao = os.path.splitext(self.caminho_do_arquivo)[1].lower()

        if extensao == ".pdf":
            with fitz.open(self.caminho_do_arquivo) as doc:
                return "\n".join([page.get_text() for page in doc])

        elif extensao == ".txt":
            with open(self.caminho_do_arquivo, "r", encoding="utf-8") as f:
                return f.read()

        else:
            raise ValueError(f"Formato de arquivo não suportado: {extensao}")


    # Script para limpeza inicial do texto 
    def limpar_texto(self, texto):
        # Remove múltiplas quebras de linha e espaços
        texto = re.sub(r'\n+', '\n', texto)     # várias quebras de linha -> uma
        texto = re.sub(r'[ \t]+', ' ', texto)   # múltiplos espaços/tabs -> um
        texto = texto.strip()
        return texto


    def separar_clausulas(self, texto):
        padrao = r'(CLÁUSULA\s+\d+º\s*-\s.*?)(?=CLÁUSULA\s+\d+º\s*-|\Z)'
        matches = re.findall(padrao, texto, flags=re.DOTALL | re.IGNORECASE)
        clausulas = [cl.strip() for cl in matches]
        return clausulas


    # Implementação da lógica de "chunking" (divisão de texto em pedaços menores)
    def gerar_chunks_para_todas_clausulas(self, tamanho_max=2000, sobreposicao=300):
        
        def gerar_chunks(texto, tamanho_max=2000, sobreposicao=300):
            chunks = []
            inicio = 0
            while inicio < len(texto):
                fim = inicio + tamanho_max
                chunk = texto[inicio:fim]
                chunks.append(chunk.strip())
                inicio += tamanho_max - sobreposicao  # move com sobreposição
            return chunks
            
        todos_chunks = []
        for i, clausula in enumerate(self.clausulas):
            chunks = gerar_chunks(clausula, tamanho_max, sobreposicao)
            for j, chunk in enumerate(chunks):
                todos_chunks.append({
                    "id": f"clausula_{i+1}_chunk_{j+1}",
                    "texto": chunk
                })
        return todos_chunks
