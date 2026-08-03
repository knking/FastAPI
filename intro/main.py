
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/about")
def about():
    return {"i am about "}

@app.get("/more")
def more():
    return "More bhai"