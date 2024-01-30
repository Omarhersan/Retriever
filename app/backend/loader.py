from langchain_community.llms import CTransformers
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import FAISS
import config
from langchain_community.embeddings import HuggingFaceEmbeddings


def load_llm(model_path: str, model_type: str = 'llama'):
    # Load locally downloaded model
    llm = CTransformers(
        model=model_path,
        model_type=model_type,
        local_files_only = True,
        config={'max_new_tokens': 600,
                'temperature': 0.01,
                'context_length': 700}
    )
    return llm

def load_embedding(data_path:str):
    loader = CSVLoader(file_path=data_path, encoding='utf-8', csv_args={'delimiter': ','})
    data = loader.load()
    # Estaría bien comentar de dónde saqué el modelo, por qué se escogió y por qué esos hiperparámetros.
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.from_documents(data, embeddings)
    db.save_local(config.DB_FAISS_PATH)
