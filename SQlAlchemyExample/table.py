from db import engine

from sqlalchemy import MetaData, Table, Integer, String, Column, ForeignKey

metadata = MetaData()

#user table

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True)
)

#one to one relation
profile = Table(
    "profile",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False,unique=True),
    Column("bio", String,nullable=False)
)

#one to many relation
posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("title", String,nullable=False),
    Column("content",String, nullable=False)
)

##----------------Many to many------------
address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("street", String, nullable=False),
    Column("city", String, nullable=False),
)

user_address_association = Table(
    "user_address_association" ,
    metadata,  
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"),primary_key=True),
    Column("address_id", Integer, ForeignKey("address.id", ondelete="CASCADE"),primary_key=True),
)


#create table in db
def creaate_table():
    metadata.create_all(engine)


