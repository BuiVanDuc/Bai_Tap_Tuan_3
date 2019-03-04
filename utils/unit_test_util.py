from main import show_list_friends, show_list_messages, add_friend
from friends.friend import show_list_friends, detail_friend
from users.user import block_user
from messages.message import show_list_messages
# if user_id exist return list friend else return 'NO friend'
# user_id =1
# show_list_messages(user_id)

list1, list2=show_list_messages(1)
print list1
print list2
# block_user(1,5)

