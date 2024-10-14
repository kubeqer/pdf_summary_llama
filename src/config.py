from dataclasses import dataclass

from user_inputs import get_doc_to_summary, get_model


@dataclass
class Config:
    document_name: str
    model: str


def get_config():
    doc = get_doc_to_summary()
    model = get_model()
    return Config(document_name=doc, model=model)
