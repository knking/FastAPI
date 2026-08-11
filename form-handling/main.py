
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()

#application/x-www-form-urlencoded
#multipart/form-data

## Simple HTMl From for testing..

@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <head>
            <title>Form Handling</title>
        </head>
        <body>
            <h1>Login Form</h1>
            <form action="/login" method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username"><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    """

#without validation
# @app.post("/login")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username, "password_length":len(password)}

#With validation
@app.post("/login")
async def login(username: Annotated[str, Form(min_length=5, max_length=15)], 
                password: Annotated[str, Form(min_length=8)]):
    return {"username": username, "password_length":len(password)}