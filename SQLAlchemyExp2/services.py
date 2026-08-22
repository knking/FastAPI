
from db import engine
from sqlalchemy import insert, asc,select,desc,func

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

# Get all users orderd by name(A-Z)

def get_users_orderd_by_name():
    with engine.connect() as con:
        st = select(users).order_by(asc(users.c.name))
        res = con.execute(st).fetchall()
        return res


# --- Get all post order by latest---

def get_post_latest_first():
    with engine.connect() as con:
        st = select(posts).order_by(desc(posts.c.id))
        res = con.execute(st).fetchall()
        return res


#Group Post by user (count how many posts each user has)
def get_post_count_per_user():
    with engine.connect() as con:
        st = select(
                posts.c.user_id,
                func.count(posts.c.id).label("Total posts")).group_by(posts.c.user_id)
        res = con.execute(st).fetchall()
        return res

# join user and posts(list all post with there author name)

def get_post_with_author():
    with engine.connect() as con:
        st = select(
                posts.c.id,
                posts.c.title,
                users.c.name.label("author name")).join(users,posts.c.user_id==users.c.id)
        res = con.execute(st).fetchall()
        return res