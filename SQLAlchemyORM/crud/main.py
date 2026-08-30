from model import create_table, drop_table
from services import *


#create table
# create_table()


# drop_table()

# create user/ insert user
# res= create_user("jk","ab@gmail.com")
# print(res)

#------------------Create/insert post-----------
# create_post(2,"post 1", "jyoti first post")

#--------Read data of user------

print(get_user_by_id(2))
print( get_post_by_id(1))

get_all_user()

update_user_email(1,"mynew@email.com")