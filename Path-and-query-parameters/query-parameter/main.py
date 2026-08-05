from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def getData():
    return {"message":"fastapi is awsome"}

#Single query parameter
# @app.get("/product")
# async def getProduct(category:str):
#     return {"you want this category things":category}

##Multiple query parameter
# @app.get("/product")
# async def getProduct(category:str, count:int):
#     return {"you want this category things":category, "number of pice":count}

#Default query parameter
# @app.get("/product")
# async def getProduct(category:str, count:int=10):
#     return {"you want this category things":category, "number of pice":count}

##Optional query parameter
# @app.get("/product")
# async def getProduct(count:int, category:str= None):
#     return {"you want this category things":category, "number of pice":count}

##Path and query parameter
@app.get("/product/{year}")
async def getProduct(year:int, count:int, category:str= None):
    return {"you want this category things":category, "number of pice":count , "year is":year}