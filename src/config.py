from pathlib import Path
import os

from dotenv import load_dotenv

# ======================================
# Carrega variáveis de ambiente
# ======================================

load_dotenv()

# ======================================
# Diretórios
# ======================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "db"

# ======================================
# OpenAI
# ======================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

OPENAI_MODEL = "gpt-5-mini"
GEMINI_MODEL = "gemini-2.5-flash"

# ======================================
# Embeddings
# ======================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ======================================
# Splitter
# ======================================

CHUNK_SIZE = 1200
CHUNK_OVERLAP = 250

# ======================================
# Retrieval
# ======================================

TOP_K = 8