from utils.cache import cached_query


def test_output_structure():
    response = cached_query("What is this document about?")

    assert hasattr(response, "answer")
    assert hasattr(response, "sources")


def test_sources_type():
    response = cached_query("test query")

    assert isinstance(response.sources, list)