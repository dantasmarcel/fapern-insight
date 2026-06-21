from openai import OpenAI
from google import genai

from src.config import (
    OPENAI_API_KEY,
    GEMINI_API_KEY,
    DEEPSEEK_API_KEY,
    OPENAI_MODEL,
    GEMINI_MODEL,
    DEEPSEEK_MODEL,
)

# ======================================
# Clientes
# ======================================

openai_client = OpenAI(
    api_key=OPENAI_API_KEY
)

gemini_client = genai.Client(
    api_key=GEMINI_API_KEY
)

deepseek_client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
)

# ======================================
# Geração de respostas
# ======================================

def generate_answer(prompt: str, model_name: str) -> str:
    """
    Envia o prompt para a LLM escolhida.

    model_name:
        - openai
        - gemini
        - deepseek
    """

    if model_name == "openai":

        response = openai_client.responses.create(
            model=OPENAI_MODEL,
            input=prompt,
        )

        return response.output_text

    elif model_name == "gemini":

        response = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        return response.text

    elif model_name == "deepseek":

        response = deepseek_client.chat.completions.create(
            model=DEEPSEEK_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content

    raise ValueError(
        f"Modelo '{model_name}' não suportado."
    )