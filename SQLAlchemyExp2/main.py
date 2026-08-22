from table import  creaate_table
from services import create_user
from services import create_post




#create table
creaate_table()

#create user
create_user("krishna","abc@gmail.com")
create_user("mohan","def@gmail.com")


#create post
create_post("1", "hello crud", "i am doing crud usig python")
create_post("1", "hello crud2", "i am doing crud usig python2")
create_post("1", "hello crud3", "i am doing crud usig python3")
create_post(2, "mohan post1", "i am mohan and i am doing crud using python")
create_post(2, "mohan 2nd post", "i am mohan and i am doing crud using python")

