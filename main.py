
from fastapi import FastAPI 

app = FastAPI()

@app.get('/')
def hello():
    return 'Hello World!'

@app.get('/info')
def info(limit=1, score:int=90):
    if score > 90:
        return {'info': f'{limit} records with score above 90 from the database'}
    else: 
        return {'info': f'{limit} records from the database'}

@app.get('/info/{id}/score')
def score(id: int):
    return {id: {'87', '91'}}

from pydantic import BaseModel 

class Student(BaseModel):
    name: str 
    id: int
    score: int 

@app.post('/info')
def create(request:Student):
    return {'record': f'New record is created with {request.name}'}

