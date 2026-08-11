
from fastapi import FastAPI, Cookie, Body
from typing import Annotated
from pydantic import BaseModel, Field
app= FastAPI()

@app.get("/")
async def home_paage():
    return {"message": "Home page "}


##cookie parameter
# @app.get("/produtcs/recommendations")
# async def get_recommendations(session_id:Annotated[ str | None, Cookie()]= None):
#     if session_id:
#         return {"message": f'Recommendation for session id {session_id}'}
#     return {"message", "No sesion id was provided "}

# class ProductCookies(BaseModel):
#     model_config= {"extra":"forbid"} ## this will restrict the extra cookie parameter, it will aloow only defined parameter
#     session_id: str 
#     preferred_category: str | None = None
#     tracking_id: str | None = None

# ## Multiple cookie parameters
# @app.get("/produtcs/recommendations")
# async def get_recommendations(cookies: Annotated[ProductCookies, Cookie()]):
#     responce = {"session_id":cookies.session_id}
#     if cookies.preferred_category:
#         responce["Message"]= f'Recomendations for {cookies.preferred_category} products'
#     else:
#         responce["Message"]= f'Default recomendations for session {cookies.session_id}'
#     if cookies.tracking_id:
#         responce["tracking_id"] = cookies.tracking_id
#     return responce

# \C:\Users\Asus>curl -H "Cookie: session_id=knr1234" http://127.0.0.1:8000/produtcs/recommendations
# ["Recommendation for session id knr1234","message"]
# C:\Users\Asus>
# C:\Users\Asus>curl -H "Cookie: session_id=knr1234" http://127.0.0.1:8000/produtcs/recommendations
# {"message":"Recommendation for session id knr1234"}
# C:\Users\Asus>curl http://127.0.0.1:8000/produtcs/recommendations
# ["message","No sesion id was provided "]
# C:\Users\Asus>
# C:\Users\Asus>curl -H "Cookie: session_id=knr1234";preferred_category=books;tracking_id=1234rt5 http://127.0.0.1:8000/produtcs/recommendations
# {"session_id":"knr1234","Message":"Recomendations for books products","tracking_id":"1234rt5"}
# C:\Users\Asus


##---------Combining with body parameter------

class ProductCookies(BaseModel):
    model_config= {"extra":"forbid"} ## this will restrict the extra cookie parameter, it will aloow only defined parameter
    session_id: str = Field(title="Session id", description="user session id")
    preferred_category: str | None = Field(default=None,title="preferred category", description="preferred category for student")

class PriceFilter(BaseModel):
    min_price: float = Field(ge=0, title="This is minmunm price")
    max_price: float = Field(default=None, title="maximum price")

## Multiple cookie parameters
@app.post("/produtcs/recommendations")
async def get_recommendations(cookies: Annotated[ProductCookies, Cookie()],
                              price_filter: Annotated[PriceFilter, Body(embed=True)]
                              ):
    responce = {"session_id":cookies.session_id}
    if cookies.preferred_category:
        responce["Message"]= f'Recomendations for {cookies.preferred_category} products'
    responce["price_range"]={"min_price":price_filter.min_price, "max-price":price_filter.max_price}
    return responce

#\Users\Asus>curl -X POST -H "Cookie: session_id=jugb567; preferred_category=books" -H "Content-Type: application/json" -d "{\"price_filter\":{\"min_price\":59.0,\"max_price\":2345.6}}" http://127.0.0.1:8000/produtcs/recommendations


# C:\Users\Asus>curl -X POST -H "Cookie: session_id=jugb567; preferred_category=books" -H "Content-Type: application/json" -d "{\"price_filter\":{\"min_price\":59.0,\"max_price\":2345.6}}" http://127.0.0.1:8000/produtcs/recommendations
# {"session_id":"jugb567","Message":"Recomendations for books products","price_range":{"min_price":59.0,"max-price":2345.6}}