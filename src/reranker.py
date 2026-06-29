from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

import torch

from src.config import (
    RERANKER_MODEL,
    RERANK_TOP_N,
)


class NeuralReranker:
    """
    Responsável por reordenar os documentos recuperados
    utilizando um modelo Transformer de reranking.
    """

    def __init__(self):

        print("🧠 Carregando Neural Reranker...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            RERANKER_MODEL
        )

        self.model = AutoModelForSequenceClassification.from_pretrained(
            RERANKER_MODEL
        )

        self.model.eval()

        print("✅ Neural Reranker carregado.")

    @torch.no_grad()
    def rerank(
        self,
        question: str,
        documents: list,
        top_n: int = RERANK_TOP_N,
    ):
        """
        Reordena documentos conforme sua relevância.
        """

        scored_docs = []

        for doc in documents:

            inputs = self.tokenizer(
                question,
                doc.page_content,
                return_tensors="pt",
                truncation=True,
                max_length=512,
            )

            logits = self.model(**inputs).logits

            score = logits.squeeze().item()

            scored_docs.append(
                {
                    "document": doc,
                    "score": score,
                }
            )

        scored_docs.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return scored_docs[:top_n]