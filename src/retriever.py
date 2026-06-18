from src.vectorstore import load_vectorstore


def get_retriever():
    """
    Retorna o retriever responsável pela busca semântica.
    """

    vectorstore = load_vectorstore()

    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 8, "fetch_k": 32}
    )