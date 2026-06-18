from src.prompts import build_prompt
from src.retriever import get_retriever
from src.llm import generate_answer


def answer(question: str):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    print("\n========== DOCUMENTOS ==========")

    for i, doc in enumerate(docs, 1):
        print(f"\nDocumento {i}")
        print(doc.metadata) 
        print(doc.page_content[:800])

    print("===============================\n")

    for i, doc in enumerate(docs, 1):
        print(f"\nDocumento {i}")
        print(doc.metadata)
        print(doc.page_content[:1000])

    print("=" * 100)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = build_prompt(question, context)

    response = generate_answer(prompt)

    sources = []

    for doc in docs:

        source = doc.metadata.get("source", "Desconhecido")
        page = doc.metadata.get("page", 0) + 1

        sources.append(
            {
                "source": source,
                "page": page,
            }
        )

    return response, sources