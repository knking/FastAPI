
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

items = {"apple":"A jucie fruit", "banana":"A yellow fruit"}

#using httpexception
# @app.get("/items/{item_name}")
# async def itesm_data(item_name:str):
#     if item_name not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return items[item_name]

#custom header
# @app.get("/items/{item_name}")
# async def itesm_data(item_name:str):
#     if item_name not in items:
#         raise HTTPException(status_code=404, 
#                             detail="Item not found",
#                             headers={"x-headers-type":"item-missing"})
#     return items[item_name]

##----------Custom exception-------------
class FruitException(Exception):
    def __init__(self, fruit_name : str):
        self.fruit_name=fruit_name

##----Custom exception handler-----
@app.exception_handler(FruitException)
async def fruit_exeption_handler(request : Request, exc:FruitException):
    return JSONResponse(status_code=408,content={"message": f"{exc.fruit_name} is not valid" })

@app.get("/items/{item_name}")
async def itesm_data(item_name:str):
    if item_name not in items:
        raise FruitException(fruit_name=item_name)
    return items[item_name]


