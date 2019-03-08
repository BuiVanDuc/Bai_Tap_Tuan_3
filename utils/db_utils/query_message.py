# query all messages is incoming
QUERY_INCOMING_MESSAGE = '''select message.sender_id, account.username, message.message_content,message.delivered_time, message.seen
from message
inner join account
on message.sender_id =account.id 
where message.recipient_id = ? order by delivered_time desc'''

# query for all messages were sent
QUERY_MESSAGE_SENT = '''select message.recipient_id, account.username, message.message_content,message.delivered_time, message.seen
from message
inner join account
on message.recipient_id =account.id
where message.sender_id = ? order by delivered_time desc'''

# query for detail message
QUERY_DETAIL_MESSAGE = '''select * from message
where (sender_id =? and recipient_id=?) or (sender_id =? and recipient_id =?) order by delivered_time asc '''

# query for update incoming message seen is true
QUERY_MESSAGE_SEEN = '''update message
set seen=1
where recipient_id=?'''

# query for sent message
QUERY_SENT_MESSAGE = '''insert into message(recipient_id, message_content, sender_id)
values(?,?,?)'''

# Query for count message unread
QUERY_MESSAGE_UNREAD ='''select count (*) as message_unread
from message
where seen =false and recipient_id=?'''

# Query for message
QUERY_MESSAGE ='''select message.sender_id, message.recipient_id, account.username, message.message_content,message.delivered_time, message.seen
from message
inner join account
on message.sender_id =account.id or message.recipient_id =account.id
where (message.sender_id  = ? or message.recipient_id=?) and account.username!='{}' order by delivered_time desc
'''