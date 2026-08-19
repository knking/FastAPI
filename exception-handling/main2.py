from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
app = FastAPI()


#-----Override default exception handler------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)

@app.get("/items/{item_id}")
async def itesm_data(item_id:int):
    return item_id



