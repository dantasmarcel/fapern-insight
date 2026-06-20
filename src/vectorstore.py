from langchain_chroma import Chroma

from src.config import DB_DIR
from src.embeddings import get_embeddings


def create_vectorstore(chunks):
    """
    Cria (ou recria) a base vetorial.
    """

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(DB_DIR),
    )

    return vectorstore


def load_vectorstore():
    """
    Carrega uma base vetorial existente.
    """

    embeddings = get_embeddings()

    return Chroma(
        persist_directory=str(DB_DIR),
        embedding_function=embeddings,
    )