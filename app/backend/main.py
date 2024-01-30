from fastapi import FastAPI
import uvicorn
from response_generator import response_call
from typing import Any, List, Union, Tuple
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    prompt:str
    session_state: List[Union[Tuple[str, str], None]]


@app.get('/')
def read_root():
    return {"message" :'Hello to the API'}

@app.get('/v0/get_response/')
def get_response(question:Question):
    answer = response_call(question.prompt, question.session_state)
    return {"Answer": answer}



if __name__ == '__main__':
    uvicorn.run('main:app', host = '0.0.0.0', port = 8000, log_level = 'info')


