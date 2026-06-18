from src.loader import load_documents
from src.splitter import split_documents
from src.vectorstore import create_vectorstore


def main():
    print("=" * 80)

    print("Carregando documentos...")
    documents = load_documents()

    print(f"Páginas carregadas: {len(documents)}")

    chunks = split_documents(documents)

    print(f"Chunks criados: {len(chunks)}")

    print("\nCriando banco vetorial...")

    create_vectorstore(chunks)

    print("Banco vetorial criado com sucesso!")

    print("=" * 80)


if __name__ == "__main__":
    main()