import streamlit as st

from src.config import (
    LLM_MODEL,
    TOP_K,
)


def render_sidebar():

    st.sidebar.title("⚙️ Configurações")

    st.sidebar.markdown("---")

    st.sidebar.markdown("### Modelo")

    model = st.sidebar.text_input(
        "LLM",
        value=LLM_MODEL,
        disabled=True,
    )

    top_k = st.sidebar.slider(
        "Top K",
        min_value=1,
        max_value=15,
        value=TOP_K,
        disabled=True,  # Por enquanto apenas informativo
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