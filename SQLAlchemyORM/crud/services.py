
from model import User, Post
from db import session_obj
from sqlalchemy import select

#----create/insert user------------

def create_user(name:str,email:str):
    with session_obj() as session:
        user=User(name=name,email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

#---------create/insert post----------------
def create_post(user_id:int,title:str,content:str):
    with session_obj() as session:
        post= Post(user_id=user_id,title=title,content=content)
        session.add(post)
        session.commit()

#---get user by id------------

def get_user_by_id(id:int):
    with session_obj() as session:
        user = session.get_one(User,id)
        return user

#-----Get post by id----------

def get_post_by_id(id:int):
    with session_obj() as session:
        stmt = select(Post).where(Post.id==id)
        post = session.scalars(stmt).one()
        return post

#-----------get all user--------
def get_all_user():
    with session_obj() as session:
        stmt = select(User)
        users= session.scalars(stmt).all()
        return users

#--------------get podst by users------

def get_all_posts_by_user(user_id:int):
    with session_obj() as session:
        user= session.get(User,user_id )
        posts = user.posts if user else []

#-----------Update email--------------------

def update_user_email(user_id:int,new_email:str):
    with session_obj() as session:
        user = session.get(User, user_id)
        if user:
            user.email = new_email
            session.commit()

        return user
