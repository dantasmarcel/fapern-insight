from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(documents):
    """
    Divide os documentos em chunks para indexação vetorial.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\nCAPÍTULO",
            "\nCapítulo",
            "\nSEÇÃO",
            "\nSeção",
            "\nArt.",
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ],
    )

    chunks = text_splitter.split_documents(documents)

    print(f"✂️ Chunks criados: {len(chunks)}")

    return chunks