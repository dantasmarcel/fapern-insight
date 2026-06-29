import time
from pathlib import Path

from src.config import ENABLE_RERANKING
from src.llm import generate_answer
from src.prompts import build_prompt
from src.retriever import get_retriever
from src.reranker import NeuralReranker

# Carrega apenas uma vez
reranker = NeuralReranker() if ENABLE_RERANKING else None


def answer(question: str, model_name: str, top_k: int):

    timings = {}

    total_start = time.perf_counter()

    # ==========================================
    # Retrieval
    # ==========================================

    retrieval_start = time.perf_counter()

    retriever = get_retriever(top_k)

    docs = retriever.invoke(question)

    timings["retrieval"] = (
        time.perf_counter() - retrieval_start
    )

    retrieved_docs = len(docs)

    # ==========================================
    # Reranking
    # ==========================================

    reranked_docs = retrieved_docs

    if ENABLE_RERANKING and reranker is not None:

        rerank_start = time.perf_counter()

        ranked_docs = reranker.rerank(
            question=question,
            documents=docs,
        )

        timings["reranker"] = (
            time.perf_counter() - rerank_start
        )

        docs = [
            item["document"]
            for item in ranked_docs
        ]

        reranked_docs = len(docs)

    else:

        timings["reranker"] = 0.0

    # ==========================================
    # Contexto
    # ==========================================

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = build_prompt(
        question=question,
        context=context,
    )

    # ==========================================
    # LLM
    # ==========================================

    llm_start = time.perf_counter()

    response = generate_answer(
        prompt,
        model_name,
    )

    timings["llm"] = (
        time.perf_counter() - llm_start
    )

    timings["total"] = (
        time.perf_counter() - total_start
    )

    # ==========================================
    # Fontes
    # ==========================================

    sources = []

    seen = set()

    for doc in docs:

        source = Path(
            doc.metadata.get(
                "source",
                "Desconhecido",
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

    metrics = {
        "retrieved_docs": retrieved_docs,
        "reranked_docs": reranked_docs,
        "timings": timings,
    }

    return response, sources, metrics