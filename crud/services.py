
from db import engine
from sqlalchemy import insert, delete, update,select

from table import users, posts

def create_user(name:str, email:str):
    with engine.connect() as connection:
        statement = insert(users).values(name=name, email=email)
        connection.execute(statement)
        connection.commit()


def create_post(user_id:int, title:str, content:str):
    with engine.connect() as connection:
        statement = insert(posts).values(user_id=user_id,title=title,content=content)
        connection.execute(statement)
        connection.commit()

#get single user by id

def get_user_by_id(user_id):
    with engine.connect() as connection:
        statement = select(users).where(users.c.id == user_id)
        result = connection.execute(statement).first()
        return result
        
# Get All Users

def get_all_users():
    with engine.connect() as connection:
        st = select(users)
        res = connection.execute(st).fetchall()
        return res

#get post by user

def get_post_by_user(user_id:int):
    with engine.connect() as connection:
        st = select(posts).where(posts.c.user_id==user_id)
        result = connection.execute(st).fetchall()
        return result

#update email
def user_email_update(user_id:int, new_email:str):
    with engine.connect() as connection:
        st = update(users).where(users.c.id == user_id).values(email=new_email)
        connection.execute(st)
        connection.commit()


# delete post
def delete_post(post_id:int):
    with engine.connect() as con:
        st = delete(posts).where(posts.c.id == post_id)
        con.execute(st)
        con.commit()