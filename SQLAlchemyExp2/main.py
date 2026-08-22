from table import  creaate_table
from services import create_user,create_post, get_users_orderd_by_name,get_post_latest_first,get_post_count_per_user,get_post_with_author
 

#create table
# creaate_table()

#create user
# create_user("krishna","abc@gmail.com")
# create_user("mohan","def@gmail.com")


# #create post
# create_post("1", "hello crud", "i am doing crud usig python")
# create_post("1", "hello crud2", "i am doing crud usig python2")
# create_post("1", "hello crud3", "i am doing crud usig python3")
# create_post(2, "mohan post1", "i am mohan and i am doing crud using python")
# create_post(2, "mohan 2nd post", "i am mohan and i am doing crud using python")

# -- get order by user name

# print(get_users_orderd_by_name())

# print(get_post_latest_first())

# print(get_post_count_per_user())

print(get_post_with_author())