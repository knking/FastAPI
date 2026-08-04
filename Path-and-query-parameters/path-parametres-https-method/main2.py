
#Path parameter with type

from fastapi import FastAPI

app = FastAPI()

#get single product
@app.get("/products/{product_id}")
async def getSingleProduct(product_id:int):
    #return {f'message:you are looking for product {product_id}' }
    return {"message":"you are looking for product" ,"prodcut_is is": product_id}   


@app.get("/products/{product_title}")
async def getSingleProduct(product_title:str):
    #return {f'message:you are looking for product {product_id}' }
    return {"message":"you are looking for product" ,"prodcut_is is": product_title}   


##Path parameter order matters

#this will execute when we give mypath
@app.get("/product/mypath")
async def product():
    return {"message": "static mypath"}

#this will execute when we give anything except than mypath
@app.get("/product/{mypath}")
async def product(mypath:str):
    return {"message": "dynamic mypath str", "path":mypath}

#this will execute when we give anything in integer
@app.get("/product/{mypath}")
async def product(mypath:int):
    return {"message": "dynamic mypath int", "path":mypath}