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
# APIs
# ======================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# ======================================
# Modelos
# ======================================

OPENAI_MODEL = "gpt-5-mini"
GEMINI_MODEL = "gemini-2.5-flash"
DEEPSEEK_MODEL = "deepseek-chat"

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

RETRIEVER_TOP_K = 8

# ======================================
# Neural Reranker
# ======================================

ENABLE_RERANKING = True

RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"

RERANK_TOP_N = 4