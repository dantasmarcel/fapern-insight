from src.config import TOP_K
from src.vectorstore import load_vectorstore


def get_retriever():
    """
    Retorna o retriever responsável pela busca semântica.
    """

    vectorstore = load_vectorstore()

    return vectorstore.as_retriever(
        search_kwargs={
            "k": TOP_K
        }
    )