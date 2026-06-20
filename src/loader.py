from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from src.config import DATA_DIR


def load_documents(data_dir: Path = DATA_DIR):
    """
    Carrega todos os arquivos PDF existentes na pasta de dados.
    """

    if not data_dir.exists():
        raise FileNotFoundError(
            f"A pasta '{data_dir}' não foi encontrada."
        )

    pdf_files = sorted(data_dir.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            f"Nenhum arquivo PDF encontrado em '{data_dir}'."
        )

    documents = []

    print("\n📚 Carregando documentos...\n")

    for pdf in pdf_files:

        print(f"✓ {pdf.name}")

        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    print(f"\nTotal de PDFs: {len(pdf_files)}")
    print(f"Total de páginas: {len(documents)}\n")

    return documents