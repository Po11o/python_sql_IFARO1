from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from rg import *

app = FastAPI()





app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
home = Jinja2Templates(directory="templates/home")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html")

@app.get("/login", response_class=HTMLResponse)
async def root(request: Request):
    return home.TemplateResponse(
        request=request, name="login.html")

@app.get("/projets")
def projets():
    return mesProjets()
