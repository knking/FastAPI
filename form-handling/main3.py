
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field
import os
import uuid
import shutil
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
            <h1>Single file upload (bytes) </h1>
            <form action="/files/" enctype="multipart/form-data" method="post">
                <label for="file">Upload file:</label>
                <input name="file" type="file"><br><br>
                <input type="submit" value="Submit">
            </form>
             <h1>Single file upload (uploadfiles) </h1>
                <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                    <label for="file">Upload file:</label>
                    <input name="file" type="file"><br><br>
                    <input type="submit" value="Submit">
                </form>
        </body>
        </html>
    """

#Single file upload
# @app.post("/files/")
# async def upload_file(file: Annotated[ bytes | None, File()]=None):
#     if not file:
#         return "No file uploaded"
#     else:
#         return {"File size": len(file)}

#-----------------save uploaded file-------------

# @app.post("/files/")
# async def upload_file(file: Annotated[ bytes | None, File()]=None):
#     if not file:
#         return {"message": "no file uploaded"}
#     filename= f'{uuid.uuid4()}.bin'
#     save_path = f'uploads/{filename}'
#     os.makedirs("uploads",exist_ok=True)

#     with open(save_path, "wb") as buffer:
#         buffer.write(file)
#     return {"file uplaod successfully with szie": len(file)}

##using uplaod file class to save file
@app.post('/uploadfiles/')
async def upload_files(file: Annotated[UploadFile | None , File()]= None):
    if not file:
        return {"Message ": "No file uploaded"}
    save_path = f'uploads/{file.filename}'
    os.makedirs("uploads", exist_ok=True)
    with open(save_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename, "Content_type":file.content_type}