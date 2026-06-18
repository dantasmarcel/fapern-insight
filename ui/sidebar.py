import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.header("⚙️ Configurações")

        model = st.selectbox(
            "Modelo",
            (
                "Mistral",
                "Gemma",
                "Llama"
            )
        )

        top_k = st.slider(
            "Quantidade de documentos recuperados",
            min_value=1,
            max_value=10,
            value=4
        )

        st.divider()

        st.subheader("📄 Base documental")

        st.success("Estatuto da FAPERN")

        st.success("Lei Complementar 257/2003")

        st.success("Decreto 17.456/2004")

        return {
            "model": model,
            "top_k": top_k
        }