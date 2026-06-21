import streamlit as st


def render_metrics(sources):

    total_fontes = len(sources)

    paginas = {
        (source["source"], source["page"])
        for source in sources
    }

    total_paginas = len(paginas)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Fontes utilizadas",
            total_fontes,
        )

    with col2:
        st.metric(
            "Páginas consultadas",
            total_paginas,
        )