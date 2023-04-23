from fastapi import FastAPI, File, Form, UploadFile, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .utils import  process_data, search
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index():
    return templates.TemplateResponse("index.html", {"request": None})

@app.post("/api/upload")
async def upload(content: str = Form(None)):
    if not content:
        return {"status": "error"}

    process_data(content)
    return {"status": "success"}


@app.get("/api/search")
async def perform_search(query: str):
    results = search(query)
    return results

@app.get("/js/main.js", response_class=Response)
async def get_main_js():
    with open("js/main.js", "r") as file:
        js_content = file.read()
    return Response(content=js_content, media_type="application/javascript")
