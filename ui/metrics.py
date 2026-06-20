import streamlit as st


def render_metrics(sources):

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Fontes utilizadas",
            len(sources),
        )

    with col2:
        st.metric(
            "Chunks recuperados",
            len(sources),
        )