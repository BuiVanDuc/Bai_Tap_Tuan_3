# Query friend
QUERY_FRIEND = '''select * from friend
where user_id=? and friend_id=?
'''

# Query for list friends
QUERY_FRIENDS_IN_MESSAGE = '''select friend.friend_id, friend.nickname
from friend
inner join message
on message.sender_id = friend.friend_id or message.recipient_id=friend.friend_id
where friend.user_id =? order by message.delivered_time desc
'''

# Query for friends
QUERY_FRIENDS = '''select friend_id, nickname from friend
where user_id =? order by nickname desc
'''

# # Query for friend not in message
# # QUERY_FRIENDS_NOT_MESSAGE = '''select friend_id, nickname from friend
# # where friend_id not in (?)
# '''

# Query for adding friend:
QUERY_ADD_FRIEND = '''insert into friend(user_id, friend_id, nickname)
values (?,?,?)
'''

# Query for edit nickname
QUERY_EDIT_NICKNAME = '''update friend
set nickname=?
where friend_id= ? 
'''

# Query for detail friend
QUERY_DETAIL_FRIEND = '''select account.fullname, account.sex, account.birth_of_date, account.username, account.lives_in
from account
where account.id=? 
'''

# Query for grouping friend by lives in
QUERY_GROUP_FRIENDS = '''select friend.friend_id,  friend.nickname, account.lives_in
from friend 
inner join account 
on friend.friend_id = account.id
where friend.user_id = ? order by account.lives_in asc 
'''

# Query searching_friend
QUERY_SEARCHING_FRIEND = '''select friend_id, nickname from friend where user_id=? and nickname like ?
'''

# Query unfriend
QUERY_UNFRIEND =''' delete from friend where user_id =? and friend_id =?
'''

# Query friend is block
QUERY_FRIEND_BLOCK ='''select friend.friend_id, friend.nickname from friend
inner join block
on friend.friend_id = block.user_id_blocked and block.user_id=?
'''
