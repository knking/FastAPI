
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

#we need to create model first
class Product(BaseModel):
    id: int
    title: str
    price: float
    stock: int | None = None


# @app.post("/products")
# async def create_product(new_prduct: Product):
#     return new_prduct

#Access pydentic attribute inside function 

# @app.post("/products")
# async def create_product(new_prduct: Product):
#     print(new_prduct.id)
#     print(new_prduct.title)
#     print(new_prduct.price)
#     print(new_prduct.stock)
#     return new_prduct

    
#Calculating value some value using pydentic model and append it back in that model and return it back to user

# @app.post("/products")
# async def create_product(new_prduct: Product):
#     updated_product = new_prduct.model_dump()
#     price_with_tax= new_prduct.price + (new_prduct.price * 18/100)
#     updated_product.update({"price_with_tax":price_with_tax})

#     return updated_product

#combining Request  body with path parameter

# @app.put("/product/{product_id}")
# async def get_product(product_id:int, new_product:Product):
#     return {"product_id":product_id, "updated_data":new_product}

##Adding query parameter

# @app.put("/product/{product_id}")
# async def get_product(product_id:int, 
#                       new_product:Product,
#                       discount: float | None= None
#                       ):
#     return {"product_id":product_id, "updated_data":new_product, "discount":discount}


##Multiple Body Parameter----------------------

class Seller(BaseModel):
    username:str
    fullName: str | None = None

# @app.post("/product")
# async def get_product(new_data: Product, new_seller : Seller):
#     return {"new data":new_data, "new Seller": new_seller}

##make body optional
# @app.post("/product")
# async def get_product(new_data: Product, new_seller : Seller | None = None):
#     return {"new data":new_data, "new Seller": new_seller}

##pass singular value to body

# @app.post("/product")
# async def get_product(new_data: Product, 
#                       new_seller : Seller, 
#                       sec_key: Annotated[str |None,  Body()]):
#     return {"new data":new_data, "new Seller": new_seller, "sec_key":sec_key}

##Embed single body parameter
##Without Embed
# @app.post("/products")
# async def create_product(new_prduct: Product):
#     return new_prduct

#with embed 

@app.post("/products")
async def create_product(new_prduct: Annotated[Product, Body(embed=True)]):
    return new_prduct