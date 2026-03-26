from langchain_core.prompts import PromptTemplate


def get_prompt(parser):
    format_instructions = parser.get_format_instructions()

    return PromptTemplate(
        input_variables=["input", "context"],
        template="""
You are a helpful assistant.

Use ONLY the provided context.

Context:
{context}

Question:
{input}

Return STRICT JSON:
{format_instructions}

Rules:
- Always include sources
- Do not hallucinate
- If unsure, say "I don't know"
""",
        partial_variables={
            "format_instructions": format_instructions
        }
    )