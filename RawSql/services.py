
from db import engine
from sqlalchemy import text

from table import users, posts

##----using RAw SQL(insert)-----------

def raw_sql_insert():
    with engine.connect() as con:
        st = text(""" 
            INSERT INTO users (name, email)
            VALUES (:name, :email)

       """)
        con.execute(st, {"name":"krishna","email":"abc2gmail.com"})
        con.commit()


# ----using RAW SQl(Select)-----------------

def raw_sql_select():
    with engine.connect() as con:
        st = text("SELECT * FROM users WHERE email = :email")
        res = con.execute(st, {"email":"abc2gmail.com"}).first()
        return res


