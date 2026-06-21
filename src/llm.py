from openai import OpenAI
from google import genai

from src.config import OPENAI_API_KEY, GEMINI_API_KEY, OPENAI_MODEL, GEMINI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)
genai_client = genai.Client(api_key=GEMINI_API_KEY)


def generate_answer(prompt: str, model_name: str) -> str:
    """
    Envia o prompt para a LLM escolhida.

    model_name: "openai" ou "gemini"
    """

    if model_name == "openai":
        response = client.responses.create(
            model=OPENAI_MODEL,
            input=prompt,
        )
        return response.output_text

    elif model_name == "gemini":
        response = genai_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )
        return response.text