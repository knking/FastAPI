
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
import uuid
import shutil
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <head>
            <title>Form Handling</title>
        </head>
        <body>
            
             <h1>User profile </h1>
                <form action="/user-with-file/" enctype="multipart/form-data" method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br><br>
                <label for="file">Profile picture </label>
                <input name="file" type="file" accept="image/*"><br><br>
                <input type="submit" value="Submit">
                </form>
        </body>
        </html>
    """

@app.post("/user-with-file/")
async def create_user_with_file(
    username : Annotated[str, Form()],
    file : Annotated[UploadFile , Form()]
):
    responce= {"username":username}

    if file:
        save_path = f'uploads/{file.filename}'
        os.makedirs('uploads', exist_ok=True)
        with open (save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        responce["filename"]= file.filename
    return responce


    

    