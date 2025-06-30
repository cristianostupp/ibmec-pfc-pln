import pytesseract
from pdf2image import convert_from_path
import os

class OCR:
    def __init__(self, pdf_path, lang="por", dpi=150):
        """
        Inicializa a classe OCR.
        :param pdf_path: Caminho do arquivo PDF
        :param lang: Idioma do OCR (ex: 'por' para português)
        :param dpi: Resolução para conversão de PDF em imagem
        """
        self.pdf_path = pdf_path
        self.lang = lang
        self.dpi = dpi
        self.paginas = []
        self.texto_por_pagina = []

    def gerar_nome_arquivo_ocr(self):
        base, _ = os.path.splitext(self.pdf_path)
        return f"{base}_ocr.txt"

    def carregar_paginas(self):
        """
        Converte o PDF em uma lista de imagens, uma por página.
        """
        self.paginas = convert_from_path(self.pdf_path, dpi=self.dpi)
        return self.paginas

    def extrair_texto(self):
        """
        Aplica OCR em cada página e armazena o texto.
        """
        if not self.paginas:
            self.carregar_paginas()

        self.texto_por_pagina = []
        for i, imagem in enumerate(self.paginas):
            texto = pytesseract.image_to_string(imagem, lang=self.lang)
            self.texto_por_pagina.append(texto)

        return self.texto_por_pagina

    def texto_unificado(self):
        """
        Retorna o texto completo concatenado, com divisões por página.
        """
        if not self.texto_por_pagina:
            self.extrair_texto()

        return "\n\n".join(
            [f"--- Página {i + 1} ---\n{pagina}" for i, pagina in enumerate(self.texto_por_pagina)]
        )

    def salvar_txt(self):
        """
        Salva o texto extraído em um arquivo .txt.
        :param output_path: Caminho para o arquivo de saída
        """
        arquivo_de_saida = self.gerar_nome_arquivo_ocr()
        texto = self.texto_unificado()
        with open(arquivo_de_saida, "w", encoding="utf-8") as f:
            f.write(texto)
        return arquivo_de_saida
