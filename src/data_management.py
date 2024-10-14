from consts import DOCS_DIR
import subprocess
from typing import List

from consts import SUMMARIES_DIR


def get_ollama_models() -> List[str]:
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
        models = result.stdout.strip().split('\n')
        models = [model.split()[0] for model in models if model and model.split()[0] != "NAME"]

        return models
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while listing Ollama models: {e}")
        return []


def get_pdf_files_from_docs_dir() -> List[str]:
    pdf_files = list(DOCS_DIR.glob('*.pdf'))
    return [pdf.name for pdf in pdf_files]


def save_summary(text, doc):
    doc = doc[:-4] + ".txt"
    with open(SUMMARIES_DIR / doc, 'w', encoding='utf-8') as file:
        file.write(text)

