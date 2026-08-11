
from fastapi import FastAPI
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def get_data():
    return {"Message":"Return type demo"}

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None

class ProductOut(BaseModel):
    name: str
    price: float

## Without retun type
# @app.get('/products')
# async def get_data():
#     return {"Status":"OK"}

##-----with retunr type annotation----
# @app.get('/products')
# async def get_data() -> Product:
#     return {
#         "id":1,
#         "name":"moble",
#         "price":4563.7,
#         "stock":2
#     }

###------ return multiple vale in the form of list----------
# @app.get('/products')
# async def get_data() -> List[Product]:
#     return [
#         { "id":1,"name":"moble","price":4563.7,"stock":2 },
#         { "id":1,"name":"moble","price":4563.7,"stock":2 },
#         { "id":1,"name":"moble","price":4563.7,"stock":2 },
#         { "id":1,"name":"moble","price":4563.7,"stock":2 }
#         ]

##------return type with Post -----------------
# @app.post('/products')
# async def create_product(product: Product) -> Product:
#     return product

# ## retun type with multiple pydentuc model

# @app.post('/products') #in this example productout will retun(it is usefull when we are doing registrationa and retuning ont username and email)
# async def create_product(product: Product) -> ProductOut:
#     return product

#-----------Example--------

class BaseUser(BaseModel):
    UserName: str 
    fullName: str

class UserIn(BaseUser):
    password: str 


@app.post('/products') 
async def create_user(user_info: UserIn) -> BaseUser:
    return user_info