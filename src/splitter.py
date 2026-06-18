from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Divide os documentos em chunks para o pipeline RAG.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    return text_splitter.split_documents(documents)