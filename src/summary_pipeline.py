from config import get_config
from data_management import save_summary
from ollama_utils import summary
from display import display_auto_summary
from display import display_answers
from ollama_utils import answer_prompt
from user_inputs import get_prompt


def summary_pipeline():
    config = get_config()
    summary_response = summary(config)
    display_auto_summary(summary_response.response)
    prompt = get_prompt()
    response = answer_prompt(
        config=config, storage_context=summary_response.storage_context, prompt=prompt
    )
    display_answers(response)
    save_summary(
        basic_summary=summary_response.response,
        answers=response,
        document_name=config.document_name,
    )
