from openai import OpenAI

from src.config import LLM_MODEL, OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)


def generate_answer(prompt: str) -> str:
    """
    Envia o prompt para a OpenAI.
    """

    response = client.responses.create(
        model=LLM_MODEL,
        input=prompt,
    )

    return response.output_text