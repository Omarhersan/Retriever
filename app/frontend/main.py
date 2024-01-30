import requests
import streamlit as st
from PIL import Image
img = Image.open('./props/retriever.jpeg')



# Define title
st.title('Welcome to the challenge chatbot')
st.text('code_name: Retriever')

with st.sidebar:
    st.write('This chatbot is created using the open-source Llama 2 LLM model from Meta.')
    st.markdown('### This chatbot was created by Omar Hernandez')
    st.image(img)

    st.link_button(label = ':dog:', url = 'https://github.com/Omarhersan')


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input('What would you like to know about the dataset?')
if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)


    # Add user message to chat history
    ''''
    Debería ser después de enviar el prompt, podría agregarse junto con la respuesta
    '''
    st.session_state.messages.append({"role": "user", "content": prompt})


    response = requests.get('http://backend:8000/v0/get_response/',
                            json={'prompt': prompt,
                                  'session_state': [tuple(("role: "+m['role'], "content: "+m['content'])) for m in st.session_state.messages]},
                            timeout=100000)
    answer = response.json()['Answer']

    # Display assistant response in chat
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

