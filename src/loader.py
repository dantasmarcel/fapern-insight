from pathlib import Path


from langchain_community.document_loaders import PyPDFLoader


def load_documents(data_path: str = "data"):
    """
    Carrega todos os PDFs existentes na pasta data.
    """

    documents = []

    pdf_files = Path(data_path).glob("*.pdf")

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    return documents