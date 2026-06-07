import streamlit as st
from groq import Groq
from src.ui.base_layout import style_base_layout
from src.pipelines.RAG import initialize_rag, generate_output
import re

@st.cache_resource
def get_client():
    return Groq(
        api_key=st.secrets["API_KEY"]
    )

def know_more():

    style_base_layout()
    if st.button("go back home"):
        st.session_state['type']=None
        st.rerun()

    st.title("Get Set Learn Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Load RAG only once
    if "retriever" not in st.session_state:
        with st.spinner("Loading knowledge base..."):
            st.session_state.retriever = initialize_rag()

    retriever = st.session_state.retriever

    # Show previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything..."):

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        client = get_client()

        with st.spinner("Searching documents..."):

            response = generate_output(
                query=prompt,
                retriever=retriever,
                client=client,
                top_k=3
            )

        response = re.sub(
            r"<think>.*?</think>",
            "",
            response,
            flags=re.DOTALL
        ).strip()

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )