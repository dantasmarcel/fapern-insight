from langchain_huggingface import HuggingFaceEmbeddings


def get_embeddings():
    """
    Retorna o modelo de embeddings utilizado pelo projeto.
    """

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )