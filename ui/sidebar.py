import streamlit as st

from src.config import TOP_K


def render_sidebar():

    st.sidebar.title("⚙️ Configurações")

    st.sidebar.markdown("---")

    st.sidebar.markdown("### Modelo")

    model = st.sidebar.selectbox(
        "Modelo de IA",
        options=["openai", "gemini"],
        index=0,
    )

    top_k = st.sidebar.slider(
        "Top K",
        min_value=1,
        max_value=23,
        value=TOP_K,
    )

    st.sidebar.markdown("---")

    st.sidebar.success("✅ Base vetorial carregada")

    st.sidebar.info(
        """
Projeto desenvolvido para a disciplina de IA Generativa.

**FAPERN Insight**
"""
    )

    return {
        "model": model,
        "top_k": top_k,
    }