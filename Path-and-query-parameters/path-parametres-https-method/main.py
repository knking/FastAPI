
from fastapi import FastAPI

app = FastAPI()

#GET request
#get all product
@app.get("/products")
async def prodcuts():
    return {"return":"All products"}

#get single product
@app.get("/products/{product_id}")
async def getSingleProduct(product_id:int):
    #return {f'message:you are looking for product {product_id}' }
    return {"message":"you are looking for product" ,"prodcut_is is": product_id}   


#POST request
#Create or Insert Data

# @app.post("/add_product")
# async def add_product(new_prodct:str):
#     return {"message":"Product created", "New product is ": new_prodct}

# @app.post("/add_product")
# async def add_product(new_prod:dict):
    
#     return {"message":"Product created", "new product created":new_prod}


#PUT Request
# Update data

# @app.put("/product/{product_id}")
# async def update(updated_product:dict,product_id:int):
#     return {"responce":"product updated ", "updated product is ":updated_product, "id_is":product_id}

#PATCH request
#Partial data updated
@app.patch("/product/{product_id}")
async def update(updated_product:dict,product_id:int):
    return {"responce":"partial data updated ", "updated product is ":updated_product, "id_is":product_id}

#DELETE request
#delete data

@app.delete("/product/{prod_id}")
async def delete(prod_id:int):
    return {"message": "data deletd" , "product id ": prod_id }

