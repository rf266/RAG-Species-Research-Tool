import requests
from fastapi import FastAPI
from functions import pipeline
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=['http://localhost:5173/']
)
@app.post('/submit')
def get_input( query:str):
    return pipeline(query)