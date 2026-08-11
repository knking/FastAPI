
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field
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
            
             <h1>Multiple file upload (uploadfiles) </h1>
                <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                    <input name="files" type="file" multiple><br><br>
                    <input type="submit" value="Upload">
                </form>
        </body>
        </html>
    """

@app.post("/uploadfiles/")
async def upload_file(files: Annotated [ list[UploadFile], File()]):
    save_files = []
    os.makedirs('uploads', exist_ok=True)
    for file in files:
        save_path = f'uploads/{file.filename}'
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        save_files.append({"file_name": file.filename})

    return save_files
    

    