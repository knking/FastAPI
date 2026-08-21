from db import engine

from sqlalchemy import MetaData, Table, Integer, String, Column

metadata = MetaData()

#user table

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True)
)

address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("street", String, nullable=False),
    Column("dist", String )
)

#create table in db
def creaate_table():
    metadata.create_all(engine)


#drop table from db
# def drop_table():
#     metadata.drop_all(engine)
