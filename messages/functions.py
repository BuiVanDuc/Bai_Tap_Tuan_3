from utils.db_utils.db_collection import query_db
from utils.db_utils.query_message import QUERY_DETAIL_MESSAGE, \
    QUERY_SENT_MESSAGE, \
    QUERY_MESSAGE_UNREAD, QUERY_MESSAGE_SEEN, QUERY_MESSAGE
from utils.db_utils.query_user import QUERY_USER_BLOCKED, QUERY_USER


def view_message(user_id, username):

    messages = query_db(QUERY_MESSAGE.format(username), (user_id, user_id,), is_data_fetched=True)

    list_ids = list()
    ret_data = list()

    # list message unread
    for message in messages:
        item = dict()
        if message['recipient_id'] == user_id:
            if message['sender_id'] not in list_ids:
                list_ids.append(message['sender_id'])

                item['id'] = message['sender_id']
                item['username'] = message['username']

                item['unread'] = 0
                if message['seen'] == 0:
                    item['unread'] = 1
                ret_data.append(item.copy())
            else:
                if message['seen'] == 0:
                    for item in ret_data:
                        if message['sender_id'] == item['id']:
                            item['unread'] += 1
    # list message sent
    for message in messages:
        item = dict()
        if message['sender_id'] == user_id:
            if message['recipient_id'] not in list_ids:
                list_ids.append(message['recipient_id'])
                item['id'] = message['recipient_id']
                item['username'] = message['username']
                ret_data.append(item.copy())

    return ret_data


def detail_message(user_id, friend_id):
    messages = query_db(QUERY_DETAIL_MESSAGE, (user_id, friend_id, friend_id, user_id,), is_data_fetched=True)

    if messages and len(messages) > 0:
        # update message seen is true
        for message in messages:
            if message['recipient_id'] == user_id:
                query_db(QUERY_MESSAGE_SEEN, (user_id, friend_id,))
        return messages
    print "Have no detail message"


def sent_message(recipient_id, message_content, sender_id):
    if is_blocked(recipient_id, sender_id):
        print "You are blocked"
        return False

    if query_db(QUERY_SENT_MESSAGE, (recipient_id, message_content, sender_id)):
        return True
    else:
        return False


def count_message_unread(user_id):
    messages_unread = query_db(QUERY_MESSAGE_UNREAD, (user_id,), is_data_fetched=True)
    return messages_unread


def is_blocked(user_id, user_blocked):
    if query_db(QUERY_USER_BLOCKED, (user_id, user_blocked,)):
        return 1
    return 0


def is_user_existed(user_id):
    if query_db(QUERY_USER, (user_id,)):
        return True
    return False