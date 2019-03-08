# Query user
QUERY_USER = ''' SELECT * FROM account
 WHERE id =?
'''
# Query for register account
QUERY_REGISTER_ACCOUNT = ''' insert into account(email, fullname, birth_of_date, sex, username, password, lives_in)
 values (?,?,?,?,?,?,?)
'''

# Query for login
QUERY_LOGIN = '''select * from account
where username=? and password=?
'''

# Query for updating status login
QUERY_STATUS_LOGIN = '''update account
set status_login = 1 
where id=?
'''

# Query logout
QUERY_LOGOUT = '''update account
set status_login = 0
where id=?
'''

# Query search username
QUERY_SEARCH_USERNAME = '''select id, username from account
where username like ? order by username asc 
'''

# Query block user
QUERY_BLOCKED_USER = '''insert into  block(user_id, user_id_blocked)
values (?,?)
'''

# Query unblock user
QUERY_UNBLOCK_USER = '''delete from block where user_id=?
'''

# Query list friends are blocked
QUERY_LIST_BLOCK = '''select * from friend.user_id_blocked, account.username
from friend
inner join account 
on friend.user_id = account.id
where account.id=?
'''

# Query for check user blocked or not
QUERY_USER_BLOCKED = '''select * from block
where user_id =? and user_id_blocked=?
'''

# Query email
QUERY_EMAIL ='''select * from account
where email like ?
'''
# Query for unblock
QUERY_UNBLOCK ='''delete from block where user_id =? and user_id_blocked=?
'''

QUERY_BLOCK = '''insert into block(user_id, user_id_blocked)
values (?,?)
'''

QUERY_LIST_BLOCK ='''select block.user_id_blocked, account.username from block
inner join account
ON block.user_id_blocked = account.id and block.user_id =?
'''

#
QUERY_INFO_BY_ID ='''select * from account where id =?
'''