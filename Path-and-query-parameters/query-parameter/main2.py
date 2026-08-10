
from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()


products = [

    {
        "id": 1,
        "name": "Wireless Mouse",
        "price": 799,
        "description": "Ergonomic wireless mouse with 2.4GHz connectivity."
    },
    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "price": 2499,
        "description": "RGB mechanical keyboard with blue switches."
    },
    {
        "id": 3,
        "name": "Bluetooth Speaker",
        "price": 1599,
        "description": "Portable Bluetooth speaker with 10-hour battery life."
    },
    {
        "id": 4,
        "name": "USB-C Hub",
        "price": 1299,
        "description": "6-in-1 USB-C hub with HDMI, USB 3.0, and SD card reader."
    },
    {
        "id": 5,
        "name": "Gaming Headset",
        "price": 2999,
        "description": "Over-ear gaming headset with noise-canceling microphone."
    },
    {
        "id": 6,
        "name": "Laptop Stand",
        "price": 999,
        "description": "Adjustable aluminum laptop stand for better ergonomics."
    },
    {
        "id": 7,
        "name": "Smart Watch",
        "price": 4999,
        "description": "Fitness tracking smartwatch with heart rate monitor."
    },
    {
        "id": 8,
        "name": "External SSD",
        "price": 6499,
        "description": "1TB portable SSD with USB 3.2 Gen 2 support."
    },
    {
        "id": 9,
        "name": "Webcam",
        "price": 2199,
        "description": "1080p Full HD webcam with built-in microphone."
    },
    {
        "id": 10,
        "name": "Power Bank",
        "price": 1799,
        "description": "20000mAh fast-charging power bank with USB-C output."
    }
]

## Basic query parameter

@app.get("/product")
async def get_product(search:str | None=None):
    if search:
        search_lower=search.lower() 
        filter_product=[]
        for product in products:
            if search_lower in product["name"].lower():
                filter_product.append(product)
        return filter_product
    return products

## Basic query parameter old way(without annnotated)
# @app.get("/product")
# async def get_product(search:str | None= Query(default=None, max_length=50, min_length=3)):
#     if search:
#         search_lower=search.lower() 
#         filter_product=[]
#         for product in products:
#             if search_lower in product["name"].lower():
#                 filter_product.append(product)
#         return filter_product
#     return products


#with annotated
# @app.get("/products")
# async def get_products(search : Annotated[str | None, Query(min_length=3,max_length=7)]=None):
#     if search:
#             search_lower=search.lower() 
#             filter_product=[]
#             for product in products:
#                 if search_lower in product["name"].lower():
#                     filter_product.append(product)
#             return filter_product
#     return products

#required parameter with annotated
# @app.get('/products')
# async def get_data(search:Annotated [str, Query(min_length=2, max_length=8)]):
#       if search:
#         search_lower=search.lower() 
#         filter_product=[]
#         for product in products:
#             if search_lower in product["name"].lower():
#                 filter_product.append(product)
#             return filter_product
#         return products

##annotation with regex
# @app.get('/products/')
# async def get_data(search: Annotated [str, Query(min_length=2, pattern="^[a-z]+$")]):
#     if search:
#         search_lower=search.lower() 
#         filter_product=[]
#         for product in products:
#             if search_lower in product["name"].lower():
#                 filter_product.append(product)
#         return filter_product
#     return products

##Multipe search iteam(Lists)
# @app.get('/products/')
# async def get_data(search: Annotated [list[str]| None, Query() ]=None):
#     if search:
#         filter_product=[]
#         for product in products:
#             for s in search:
#                 if s.lower() in product["name"].lower():
#                     filter_product.append(product)
#         return filter_product
#     return products


##alias 

# @app.get('/products')
# async def get_data(search: Annotated [str | None, Query(alias="q")]=None):
#     if search:
#         search_lower=search.lower() 
#         filter_product=[]
#         for product in products:
#             if search_lower in product["name"].lower():
#                 filter_product.append(product)
#         return filter_product
#     return products

##meta data 
# @app.get('/products')
# async def get_data(search: Annotated [
#     str | None, 
#     Query(alias="q", title="search product", description="search by product name")

#     ]=None):
#     if search:
#         search_lower=search.lower() 
#         filter_product=[]
#         for product in products:
#             if search_lower in product["name"].lower():
#                 filter_product.append(product)
#         return filter_product
#     return products

##Adding deprecation
@app.get('/products')
async def get_data(search: Annotated [
    str | None, 
    Query(alias="q", title="search product", description="search by product name",
          deprecated=True)

    ]=None):
    if search:
        search_lower=search.lower() 
        filter_product=[]
        for product in products:
            if search_lower in product["name"].lower():
                filter_product.append(product)
        return filter_product
    return products

#custom validator

def check_valid_id(id:str):
    if not id.startswith("prod-"):
        raise ValueError("ID Must start with prod -")
    return id

@app.get("/products")
async def get_Products(id: Annotated[ str | None , AfterValidator(check_valid_id)]= None):
    if id:
        return { "id": id , "message":" valid product"}