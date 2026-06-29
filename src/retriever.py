from src.config import RETRIEVER_TOP_K
from src.vectorstore import load_vectorstore


def get_retriever(top_k: int = RETRIEVER_TOP_K):
    """
    Retorna o retriever responsável pela busca semântica.
    """

    vectorstore = load_vectorstore()

    return vectorstore.as_retriever(
        search_kwargs={
            "k": top_k
        }
    )