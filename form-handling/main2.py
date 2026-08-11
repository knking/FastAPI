

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel,Field

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

# class FormData(BaseModel):
#     username: str
#     password:str

#pydantic model for form

# @app.post("/login")
# async def login(data:Annotated[FormData, Form()]):
#     return {"username": data.username, "password_length":len(data.password)}

class FormData(BaseModel):
    model_config={"extra":"forbid"}
    username: str = Field(min_length=3, max_length=10)
    password:str = Field(min_length=5)


#pydantic model for form with validation
# @app.post("/login")
# async def login(data:Annotated[FormData, Form()]):
#     return {"username": data.username, "password_length":len(data.password)}
