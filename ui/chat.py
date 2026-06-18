import streamlit as st

from src.rag import answer


def render_chat(config):

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibe o histórico
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Mostra as fontes somente nas mensagens do assistente
            if (
                message["role"] == "assistant"
                and "sources" in message
                and message["sources"]
            ):
                with st.expander("📚 Fontes utilizadas"):
                    for source in message["sources"]:
                        st.markdown(
                            f"**{source['source']}** — Página {source['page']}"
                        )

    question = st.chat_input(
        "Faça uma pergunta sobre os documentos..."
    )

    if question:

        # Mostra a pergunta
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Consulta o RAG
        with st.chat_message("assistant"):

            with st.spinner("Consultando os documentos..."):

                response, sources = answer(question)

            st.markdown(response)

            if sources:

                with st.expander("📚 Fontes utilizadas"):

                    for source in sources:

                        st.markdown(
                            f"**{source['source']}** — Página {source['page']}"
                        )

        # Salva no histórico
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
                "sources": sources,
            }
        )