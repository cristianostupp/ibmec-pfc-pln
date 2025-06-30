# 🧠 Decodificador de Acordos Coletivos de Trabalho (PLN + LLM)

Este projeto tem como objetivo automatizar a extração, o pré-processamento e a análise de documentos de Acordos Coletivos de Trabalho, mesmo quando estão em formato digitalizado (PDF com imagem). Ele utiliza técnicas de **OCR (Reconhecimento Óptico de Caracteres)**, **processamento de linguagem natural (PLN)** e divisão inteligente de cláusulas contratuais.

---

## 🚀 Funcionalidades

- ✅ Suporte a PDFs com **texto nativo** ou **escaneado**
- 🧾 Extração de cláusulas contratuais com reconhecimento de padrões legais
- 🧠 Pré-processamento e limpeza textual
- ✂️ Divisão em **chunks otimizados para LLMs**
- 🧪 Pronto para uso com embeddings (FAISS, OpenAI, etc.)

---

## 📂 Estrutura do Projeto

```bash
.
├── src/
│   ├── ocr.py                    # Classe OCR (extração de texto via Tesseract)
│   ├── decodificador_de_normas.py # Separação de cláusulas e pré-processamento
│   ├── main.py                  # Execução principal
├── files/                       # PDFs de entrada
├── output/                      # Saída dos textos extraídos
├── requirements.txt            # Dependências do projeto
└── README.md
