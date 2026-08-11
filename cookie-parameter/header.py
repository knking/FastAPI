
from fastapi import FastAPI, Header, Body
from typing import Annotated
from pydantic import Field, BaseModel

app = FastAPI()
##header parameter
# @app.get('/product')
# async def get_produtcs( user_agent: Annotated[ str | None, Header()] = None):
#     return user_agent


##Handling duplicate headers
# @app.get('/product')
# async def get_produtcs(x_product_token: Annotated[ list[str] | None, Header()] = None):
#     return {
#         "x_Product_token": x_product_token or []
#     }


# C:\Users\Asus>curl -H "X-Product-Token:token1" -H "X-Product-Token:token2" http://127.0.0.1:8000/product
# {"x_Product_token":["token1","token2"]}
# C:\Users\Asus>

#--------Header parametr with pydentic model--------

class ProductsHeader(BaseModel):
    model_config={"extra":"forbid"}
    authorization : str
    accept_language : str | None = None
    x_tracking_id : list[str] = []

@app.get('/product')
async def get_produtcs(headers: Annotated[ ProductsHeader, Header()] = None):
    return {
        "headers": headers
    }

# >curl -H "Authorization:Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id:track1" -H "X-Tracking-Id:track2" http://127.0.0.1:8000/product
# {"headers":{"authorization":"Bearer token123","accept_language":"en-US","x_tracking_id":["track1","track2"]}}
# C:\Users\Asus>