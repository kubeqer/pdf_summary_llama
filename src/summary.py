from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

from consts import DOCS_DIR
from data_management import save_summary


def summary(doc: str, model: str, prompt: str) -> str:
    complete_prompt =f"""<s>[INST] <<SYS>>
    You are a researcher task with answering questions about an article.  
    If you don't know the answer, please don't share false information.
    <</SYS>>
    {prompt}
    [/INST]"""
    document = SimpleDirectoryReader(input_files=[DOCS_DIR / doc]).load_data()
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    Settings.llm = Ollama(model=model, request_timeout=360.0)
    index = VectorStoreIndex.from_documents(
    document,
    )

    query_engine = index.as_query_engine()
    response = str(query_engine.query(complete_prompt))
    save_summary(response, doc)
    return response