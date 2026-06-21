import streamlit as st

from ui.metrics import render_metrics
from src.rag import answer


def render_chat(config):

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message.get("sources"):

                with st.expander("📚 Fontes utilizadas"):

                    for source in message["sources"]:

                        st.write(
                            f"**{source['source']}** — Página {source['page']}"
                        )

    question = st.chat_input(
        "Faça uma pergunta sobre os documentos..."
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Consultando documentos..."):

            response, sources = answer(
                question=question,
                model_name=config["model"],
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
                "sources": sources,
            }
        )

        with st.chat_message("assistant"):

            st.markdown(response)

            render_metrics(sources)

            with st.expander("📚 Fontes utilizadas", expanded=False):

                for source in sources:

                    st.write(
                        f"**{source['source']}** — Página {source['page']}"
                    )