from langchain_core.output_parsers import PydanticOutputParser
from schemas.response import QAResponse


EXAMPLE_FORMAT = """Return ONLY a JSON object. No explanation before or after. Example:
{
  "answer": "your full answer here",
  "sources": [
    {
      "content": "the exact passage from the document you used",
      "source": "path/to/the/file.docx"
    }
  ]
}"""


class LlamaFriendlyParser(PydanticOutputParser):
    """
    PydanticOutputParser subclass that overrides get_format_instructions()
    to return a concrete JSON example instead of the auto-generated schema.
    Llama3 follows examples reliably; abstract $ref/$defs schemas confuse it.
    parser.parse() still runs full Pydantic validation unchanged.
    """

    def get_format_instructions(self) -> str:
        return EXAMPLE_FORMAT


def get_output_parser():
    return LlamaFriendlyParser(pydantic_object=QAResponse)