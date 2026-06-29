import streamlit as st

from src.config import RETRIEVER_TOP_K


MODELS = {
    "🤖 GPT-5 Mini (OpenAI)": "openai",
    "✨ Gemini 2.5 Flash": "gemini",
    "🧠 DeepSeek Chat": "deepseek",
}


def render_sidebar():

    st.sidebar.title("⚙️ Configurações")

    st.sidebar.divider()

    st.sidebar.subheader("Modelo de IA")

    selected_model = st.sidebar.selectbox(
        label="Escolha o modelo",
        options=list(MODELS.keys()),
        index=0,
        help="Selecione a LLM que será utilizada para responder às perguntas.",
    )

    st.sidebar.subheader("Recuperação de Contexto")

    top_k = st.sidebar.slider(
        "Quantidade de trechos recuperados",
        min_value=1,
        max_value=20,
        value=RETRIEVER_TOP_K,
        help="Número de trechos recuperados antes da geração da resposta.",
    )

    st.sidebar.divider()

    st.sidebar.success("✅ Base vetorial carregada")

    st.sidebar.info(
        """
### FAPERN Insight

Assistente inteligente baseado em **RAG (Retrieval-Augmented Generation)** para consulta aos documentos institucionais da FAPERN.

#### Recursos

- 📄 Busca semântica em documentos
- 🤖 Suporte a múltiplas LLMs
- 📚 Exibição das fontes utilizadas
- ⚡ Recuperação vetorial com ChromaDB
"""
    )

    return {
        "model": MODELS[selected_model],
        "top_k": top_k,
    }