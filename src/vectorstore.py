from langchain_chroma import Chroma

from src.embeddings import get_embeddings


DB_DIRECTORY = "db"


def create_vectorstore(chunks):
    """
    Cria (ou recria) a base vetorial.
    """

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIRECTORY
    )

    return vectorstore


def load_vectorstore():
    """
    Carrega uma base vetorial já existente.
    """

    embeddings = get_embeddings()

    return Chroma(
        persist_directory=DB_DIRECTORY,
        embedding_function=embeddings
    )