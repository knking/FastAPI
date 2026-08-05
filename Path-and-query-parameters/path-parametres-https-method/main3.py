
from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class allowedcategory(str,Enum):
    books="books"
    clothing="jeans"
    electronics="mobile"


@app.get("/")
async def prodcut():
    return "hello from fastapi"

# @app.get("/product/{category}")
# async def prodcut(category:allowedcategory):
#     return {"responce":"product fetched", "category is ": category}

##working with python enumeration

# @app.get("/product/{category}")
# async def prodcut(category:allowedcategory):
#     if category == allowedcategory.books:
#         return {"responce":"Books are awsome"}
#     elif category.value=="jeans":
#         return {category.value: "Clothing is cool"}
#     elif category == allowedcategory.electronics.value:
#         return {"responce":"mobile are awsome"}
#     else:
#         return {"responce": " Unknown category"}

    

##-----------Path convertor------------

@app.get("/files/{file_path:path}")
async def myfilePath(file_path:str):
    return {"Your Specified path is ": file_path}
