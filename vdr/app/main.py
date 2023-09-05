#-*- coding:utf-8 -*-
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/registrar/{did_doc}")
def register(did_doc:str) -> bool:
    pass

@app.get("/resolver/{did}")
def search(did:str) -> str:
    pass