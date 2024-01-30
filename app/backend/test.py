import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []


prompt = ''
# Add user message to chat history
st.session_state.messages.append({"role": "user", "content": prompt})

output = [("role: "+m['role'], "content: "+m['content']) for m in st.session_state.messages]

st.text(output)
