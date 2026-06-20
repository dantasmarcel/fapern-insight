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

LLM_MODEL = "gpt-5-mini"

# ======================================
# Embeddings
# ======================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ======================================
# Splitter
# ======================================

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# ======================================
# Retrieval
# ======================================

TOP_K = 23