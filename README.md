# 🤖 FAPERN Insight

Assistente Inteligente para Consulta de Documentos Institucionais da FAPERN utilizando **Retrieval-Augmented Generation (RAG)**.

O projeto foi desenvolvido como atividade da disciplina de **Inteligência Artificial Generativa** do **Instituto Metrópole Digital (IMD/UFRN)**.

---

# 📖 Sobre o projeto

O **FAPERN Insight** é um sistema que utiliza técnicas de **Retrieval-Augmented Generation (RAG)** para responder perguntas baseadas exclusivamente em documentos oficiais da **Fundação de Amparo e Promoção da Ciência, Tecnologia e Inovação do Rio Grande do Norte**.

Em vez de responder utilizando conhecimento geral da IA, o sistema realiza uma busca semântica em uma base de documentos institucionais indexados e utiliza apenas essas informações para construir a resposta.

---

# 🎯 Objetivo

Desenvolver um assistente inteligente capaz de:

- Consultar documentos institucionais da FAPERN;
- Responder perguntas em linguagem natural;
- Apresentar as fontes utilizadas em cada resposta;
- Reduzir alucinações da LLM utilizando a técnica RAG.

---

# 🏛 Base documental

A base utilizada é composta por documentos oficiais da FAPERN, incluindo:

- Estatuto da FAPERN;
- Leis Complementares;
- Decretos;
- Resoluções.

### Base atual

- 📄 **23 documentos PDF**
- 📚 **236 páginas**
- ✂️ **1259 chunks indexados**

---

# 🏗 Arquitetura

```text
PDFs
    │
    ▼
Loader (PyPDFLoader)
    │
    ▼
Splitter
(RecursiveCharacterTextSplitter)
    │
    ▼
Embeddings
(sentence-transformers/all-MiniLM-L6-v2)
    │
    ▼
ChromaDB
(Vector Store)
    │
    ▼
Retriever
    │
    ▼
OpenAI GPT-5 mini
    │
    ▼
Resposta
```

---

# 🛠 Tecnologias utilizadas

## Linguagem

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)

## Interface

![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red?logo=streamlit)

## Framework RAG

![LangChain](https://img.shields.io/badge/LangChain-RAG-green)

## Banco Vetorial

![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-orange)

## Embeddings

- sentence-transformers/all-MiniLM-L6-v2

## Modelo de Linguagem

![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5--mini-black)

## Leitura de documentos

![PyPDF](https://img.shields.io/badge/PyPDF-PDF%20Loader-blue)

---

# 📂 Estrutura do projeto

```text
fapern-insight/

├── app.py
├── index_documents.py
├── data/
├── db/
├── src/
│   ├── config.py
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── retriever.py
│   ├── prompts.py
│   ├── rag.py
│   └── llm.py
│
├── ui/
│   ├── chat.py
│   ├── header.py
│   ├── sidebar.py
│   └── metrics.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/dantasmarcel/fapern-insight.git
```

Entre na pasta do projeto:

```bash
cd fapern-insight
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuração

Crie um arquivo `.env` na raiz do projeto contendo:

```env
OPENAI_API_KEY=sua_chave_da_openai
```

---

# 📚 Indexação dos documentos

Após adicionar ou atualizar documentos na pasta `data/`, execute:

```bash
python index_documents.py
```

Esse comando irá:

- Carregar todos os PDFs;
- Dividir os documentos em chunks;
- Gerar os embeddings;
- Criar o banco vetorial ChromaDB.

---

# ▶️ Executando o sistema

```bash
streamlit run app.py
```

---

# 💬 Exemplos de perguntas

- O que é a FAPERN?
- Qual a finalidade da FAPERN?
- Como é composta a Diretoria da FAPERN?
- O que estabelece a Lei nº 14.133/2021?
- Quais são as competências do Diretor-Presidente?
- O que dispõe a Lei Complementar nº 257/2003?

---

# 📊 Resultados

O sistema é capaz de:

- Responder perguntas em linguagem natural;
- Recuperar documentos relevantes utilizando busca vetorial;
- Apresentar as fontes utilizadas em cada resposta;
- Reduzir respostas sem fundamentação utilizando a técnica RAG.

---

# 🚀 Trabalhos futuros

- Busca híbrida (vetorial + palavras-chave);
- Reranking dos documentos recuperados;
- Upload de novos documentos pela interface;
- Filtros por tipo de documento;
- Histórico persistente de conversas;
- Dashboard administrativo.

---

# 👨‍💻 Autor

**Marcel Dantas**

Graduado em Tecnologia em Ciência de Dados

Instituto Metrópole Digital (IMD/UFRN)

---

# 📄 Licença

> Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de **Inteligência Artificial Generativa** do Instituto Metrópole Digital (IMD/UFRN).

![License](https://img.shields.io/badge/License-Academic-lightgrey)
