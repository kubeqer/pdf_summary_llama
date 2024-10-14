from dataclasses import dataclass


@dataclass
class SummaryResponse:
    response: str
    storage_context: dict
