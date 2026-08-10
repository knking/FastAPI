
from fastapi import FastAPI,Body
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

##we can put some extra validation to pydentic field

# class Product(BaseModel):
#     id: int = Field(ge=1,name="Id of product")
#     name: str = Field(name="name of product", description="This is name of product",
#                       max_length=30,pattern="^[a-zA-Z]+$")
#     price : float = Field(name="price of product", gt=0)
#     stock : int | None = Field(default=None, gt=0)


# @app.post("/products")
# async def create_product(new_prduct: Product):
#     return {"New_product": new_prduct}

##nested body models
#sub model
# class Category(BaseModel):
#     name :str = Field(name='This is name ', max_length=100)
#     description: str = Field(name="i m description")

# class Product(BaseModel):
#     id: int = Field(ge=1,name="Id of product")
#     name: str = Field(name="name of product", description="This is name of product",
#                       max_length=30,pattern="^[a-zA-Z]+$")
#     price : float = Field(name="price of product", gt=0)
#     stock : int | None = Field(default=None, gt=0)
#     category : Category


# @app.post("/products")
# async def create_product(new_prduct: Product):
#     return {"New_product": new_prduct}


#----pydentic body example value----------------
#using field example we can give example value to pydentic model field and it will be shown in swagger ui
# class Product(BaseModel):
#     id: int = Field(example=1)
#     name: str = Field(example="Power Bank")
#     price : float = Field(example=1799.0)
#     stock : int | None = Field(default=None, example=100)

# @app.post("/products")
# async def create_product(new_prduct: Product):
#     return {"New_product": new_prduct}  

##----- using pydentic's json_schema_extra we can give example value to pydentic model field and it will be shown in swagger ui
class Product(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="Power Bank")
    price : float = Field(example=1799.0)
    stock : int | None = Field(default=None, example=100)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 10,
                "name": "Power Bank",
                "price": 1799,
                "description": "20000mAh fast-charging power bank with USB-C output."
            }
        }
    }
@app.post("/products")
async def create_product(new_prduct: Product):
    return {"New_product": new_prduct}  



   
