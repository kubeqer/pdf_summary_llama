from llama_index.core import (
    Settings,
    DocumentSummaryIndex,
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.readers.file import PDFReader

from consts import DOCS_DIR
from data_management import save_summary


def summary(doc: str, model: str, prompt: str) -> str:
    complete_prompt = f"""<s>[INST] <<SYS>>
    You are a researcher task with answering questions about an article.  
    If you don't know the answer, please don't share false information.
    <</SYS>>
    {prompt}
    [/INST]"""
    document = PDFReader(return_full_document=True).load_data(DOCS_DIR / doc)
    index = DocumentSummaryIndex.from_documents(
        document,
        embed_model=HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5"),
        llm=Ollama(model=model, request_timeout=360.0, temperature=0),
        show_progress=True,
    )

    query_engine = index.as_query_engine(response_mode="tree_summarize", use_async=True)
    auto_summary = index.get_document_summary(document[0].doc_id)
    print(f"SUMMARY:\n{str(auto_summary)}")
    response = str(query_engine.query(complete_prompt))


    save_summary(response, doc)
    return response
