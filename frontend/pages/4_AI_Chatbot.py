import streamlit as st
import requests

st.title("🤖 AI Business Analytics Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask a business question...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    
    response = requests.post(
            "http://127.0.0.1:8000/chat",
            params={
                "question": prompt
            }
        )

        
    answer = response.json()["answer"]

    with st.chat_message("assistant"):
                st.write(answer)

    st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        