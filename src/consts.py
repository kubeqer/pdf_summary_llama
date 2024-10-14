from pathlib import Path

ROOT_DIR = Path(__file__).parents[1]
DOCS_DIR = ROOT_DIR / "docs"
SUMMARIES_DIR = ROOT_DIR / "summaries"

DOCS_DIR.mkdir(parents=True, exist_ok=True)
SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)