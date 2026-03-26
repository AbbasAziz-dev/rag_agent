from functools import lru_cache
from agent.rag_agent import get_rag_chain


@lru_cache(maxsize=100)
def cached_query(query: str):
    chain, parser = get_rag_chain()

    result = chain.invoke(query)  # ✅ FIXED

    try:
        return parser.parse(result)
    except Exception:
        return {
            "answer": result,
            "sources": []
        }