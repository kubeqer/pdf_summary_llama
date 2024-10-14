from llama_index.core import (
    Settings,
    DocumentSummaryIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.readers.file import PDFReader
from consts import DOCS_DIR
from summary_response import SummaryResponse
from config import Config


def summary(config: Config) -> SummaryResponse:
    document = PDFReader(return_full_document=True).load_data(
        DOCS_DIR / config.document_name
    )

    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    Settings.llm = Ollama(model=config.model, request_timeout=360.0, temperature=0)

    index = DocumentSummaryIndex.from_documents(
        document,
        show_progress=True,
    )

    response = index.get_document_summary(document[0].doc_id)
    storage_context = index.storage_context.to_dict()
    return SummaryResponse(response=response, storage_context=storage_context)


def answer_prompt(config: Config, storage_context: dict, prompt: str) -> str:
    complete_prompt = f"""<s>[INST] <<SYS>>
    You are a researcher task with answering questions about an article.  
    If you don't know the answer, please don't share false information.
    <</SYS>>
    {prompt}
    [/INST]"""

    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    Settings.llm = Ollama(model=config.model, request_timeout=360.0, temperature=0)
    storage = StorageContext.from_dict(storage_context)
    index = load_index_from_storage(storage_context=storage)
    query_engine = index.as_query_engine()
    response = str(query_engine.query(complete_prompt))
    return response
