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

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("title", String,nullable=False),
    Column("content",String, nullable=False)
)



#create table in db
def creaate_table():
    metadata.create_all(engine)


