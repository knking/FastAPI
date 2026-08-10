#Path parameter validator

from fastapi import FastAPI, Path, Query
from typing import Annotated

app= FastAPI()

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
    }
]

##basic path parameter
# @app.get("/product/{product_id}")
# async def get_product(id:int):
#     for product in products:
#         if product["id"]== id:
#             return product
#     return {"error":"product not found"}

## Numeric validation in path parameter
@app.get("/product/{product_id}")
async def get_product(product_id: Annotated[int, Path(ge=1)],
                      search : Annotated[str | None, Query(max_length=10)]):
    for product in products:
        if product["id"]== product_id:
            if search and search.lower() not in product["name"]:
                return {"error": "product does not match search term"}
            return product

            
    return {"error":"product not found"}

##combine path and query parameter
