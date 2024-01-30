from loader import load_llm, load_embedding
from langchain.chains import ConversationalRetrievalChain
from config import DB_FAISS_PATH, MODEL_PATH, DATA_PATH
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import Any

def response_call(prompt:str, session_state:Any):
    ''''
    Cada llamada a response_call carga otra vez el modelo, no debería ser así
    Usa mucha memoria porque lo carga cada vez que se llama

    Debería ser una clase con un método call
    '''
    load_embedding(DATA_PATH)
    db = FAISS.load_local(DB_FAISS_PATH, HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                                               model_kwargs={'device': 'cpu'}))
    llm = load_llm(MODEL_PATH, model_type='llama')
    chain = ConversationalRetrievalChain.from_llm(llm=llm,
                                                  retriever=db.as_retriever())

    response = chain({'question': prompt,
                      'chat_history': session_state})
    result = response['answer']
    return result
