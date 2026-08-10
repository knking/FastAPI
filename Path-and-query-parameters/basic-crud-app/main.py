
from fastapi import FastAPI, status

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

@app.get("/")
async def mydata():
    return {"message":"Hit the other path for data"}

@app.get("/products",status_code=status.HTTP_200_OK)
async def getData():
    return products


@app.get("/products/name/{name}")
async def getData(name:str):
    for prodcut in products:
        if prodcut["name"]==name:
            return {"you requested for ": prodcut} 
    return "product not found in db"


@app.get("/products/id/{id}")
async def getData(id:int):
    for prodcut in products:
        if prodcut["id"]==id:
            return {"you requested for ": prodcut}
    return "product not found in db"

#post or create data

@app.post("/products",status_code=status.HTTP_201_CREATED)
async def create_product(new_data:dict):
    products.append(new_data)
    return products

#PUT or update data
@app.put("/products/{id}")
async def update_product(id:int,updated_data:dict):
    for index,product in enumerate(products):
        if product["id"]== id:
            products[index]=updated_data

            return products

##PATCH
## Update partial data

@app.patch("/products/{id}")
async def partial_update(id:int, partial_data:dict):
    for product in products:
        if product["id"] == id:
            product.update(partial_data)

            return products


##DELETE
## Delete data

# @app.delete("/products/{id}")
# async def delete_data(id:int):
#     for product in products:
#         if product["id"] == id:
#             products.remove(product)

#             return products

@app.delete("/products/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_data(id:int):
    for index,product in enumerate(products):
        if product["id"]==id:
            products.pop(index)

            # return products
            ##When we are deleting something then its good practice to return code 204