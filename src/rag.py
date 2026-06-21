from pathlib import Path

from src.llm import generate_answer
from src.prompts import build_prompt
from src.retriever import get_retriever


def answer(question: str, model_name: str):
    """
    Pipeline principal do RAG.
    """

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = build_prompt(
        question=question,
        context=context,
    )

    response = generate_answer(
        prompt,
        model_name,
    )

    sources = []

    seen = set()

    for doc in docs:

        source = Path(
            doc.metadata.get(
                "source",
                "Desconhecido"
            )
        ).stem.replace("_", " ").title()

        page = doc.metadata.get("page", 0) + 1

        key = (source, page)

        if key not in seen:

            seen.add(key)

            sources.append(
                {
                    "source": source,
                    "page": page,
                }
            )

    return response, sources