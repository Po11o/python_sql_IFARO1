from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from RG import *

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/projets")
def projets():
    return mesProjets()
