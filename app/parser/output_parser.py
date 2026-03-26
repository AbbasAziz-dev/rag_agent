from langchain_core.output_parsers import PydanticOutputParser
from schemas.response import QAResponse


def get_output_parser():
    """Create parser for structured output."""
    return PydanticOutputParser(pydantic_object=QAResponse)