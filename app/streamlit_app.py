import streamlit as st
from utils.cache import cached_query

st.title("📄 RAG Q&A System")

query = st.text_input("Ask a question")

if query:
    response = cached_query(query)

    st.subheader("Answer")
    st.write(response.answer)

    st.subheader("Sources")
    for src in response.sources:
        st.write("-", src.source)