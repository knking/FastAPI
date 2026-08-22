
from db import engine
from sqlalchemy import insert, delete, update,select

from table import users, posts

# inser or create user

def create_user(name:str, email:str):
    with engine.connect() as connection:
        statement = insert(users).values(name=name, email=email)
        connection.execute(statement)
        connection.commit()

# inser or create post

def create_post(user_id:int, title:str, content:str):
    with engine.connect() as connection:
        statement = insert(posts).values(user_id=user_id,title=title,content=content)
        connection.execute(statement)
        connection.commit()

