import streamlit as st

from utils.chat_engine import (
    ask_resume_question
)


def show_chat():

    st.title(
        "🤖 AI Career Assistant"
    )

    if "messages" not in st.session_state:

        st.session_state.messages = []

    for msg in st.session_state.messages:

        with st.chat_message(
            msg["role"]
        ):

            st.write(
                msg["content"]
            )

    prompt = st.chat_input(
        "Ask anything..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message(
            "user"
        ):

            st.write(prompt)

        if (
            "retriever"
            not in st.session_state
        ):

            answer = (
                "Please analyze "
                "a resume first."
            )

        else:

            answer = ask_resume_question(
                st.session_state[
                    "retriever"
                ],
                prompt
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message(
            "assistant"
        ):

            st.write(answer)