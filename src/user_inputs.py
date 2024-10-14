from data_management import get_pdf_files_from_docs_dir, get_ollama_models


def get_doc_to_summary() -> str:
    docs = get_pdf_files_from_docs_dir()
    docs_str = ", ".join(docs)
    doc_to_summary = input(f"Pass me the doc to summary. You can choose: {docs_str}\n")
    if doc_to_summary not in docs:
        print(f"ERROR: Provided value is not in the docs directory. {doc_to_summary}\n")
        raise ValueError
    return doc_to_summary


def get_model() -> str:
    models = get_ollama_models()
    models_str = ", ".join(models)
    model_to_summary = input(f"Pass me the model to use. You have installed: {models_str}\n")
    if model_to_summary not in models:
        print(f"ERROR: Provided value is not available. {model_to_summary}")
    return model_to_summary


def get_prompt() -> str:
    prompt = input("Ask me a question or give me a task!\n")
    return prompt
