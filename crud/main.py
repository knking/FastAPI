from table import  creaate_table
from services import create_user, get_user_by_id, get_all_users, get_post_by_user,user_email_update,delete_post
# from services import *
from services import create_post




#create table
# creaate_table()

#create user
# create_user("krishna","abc@gmail.com")
# create_user("mohan","def@gmail.com")
#create post
# create_post("1", "hello crud", "i am doing crud usig python")
# create_post(2, "mohan post", "i am mohan and i am doing crud using python")
# create_post(2, "mohan 2nd post", "i am mohan and i am doing crud using python")

#get user data

# print(get_user_by_id(1))

##Get all users
# print(get_all_users())

# get post by user
# print(get_post_by_user(2))
# user_email_update(1,"emailupdate@gmail.com")

##Delete post

delete_post(2)