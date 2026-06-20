from src.loader import load_documents
from src.splitter import split_documents
from src.vectorstore import create_vectorstore


def main():
    print("=" * 80)
    print("🚀 FAPERN Insight - Indexação de Documentos")
    print("=" * 80)

    # Carrega os documentos
    documents = load_documents()

    # Divide em chunks
    chunks = split_documents(documents)

    # Cria o banco vetorial
    create_vectorstore(chunks)

    print("\n✅ Banco vetorial criado com sucesso!")
    print(f"📄 Total de páginas: {len(documents)}")
    print(f"✂️ Total de chunks: {len(chunks)}")
    print("=" * 80)


if __name__ == "__main__":
    main()