from utils.checking_data_util import is_blocked
from utils.db_util import query_db


def show_list_messages(user_id):
    # messages sent to friend
    query_message_sent = "SELECT message.recipient_id, user_messenger.username, message.message_content, message.delivered_time, message.seen\t" \
                         "FROM message\t" \
                         "INNER JOIN user_messenger\t" \
                         "ON message.recipient_id =user_messenger.id\t" \
                         "WHERE message.sender_id ={}\tORDER BY delivered_time DESC".format(user_id)

    # incoming message
    query_incoming_message = "SELECT message.sender_id, user_messenger.username, message.message_content, message.delivered_time, message.seen\t" \
                             "FROM message\t" \
                             "INNER JOIN user_messenger\t" \
                             "ON message.sender_id =user_messenger.id\t" \
                             "WHERE message.recipient_id ={}\tORDER BY delivered_time DESC".format(user_id)

    ret_incoming_messages = list()
    ret_messages_sent = list()

    # all incoming messages
    list_incoming_messages = query_db(query_incoming_message, is_data_fetched=True)
    # Group incoming message by id and username
    """
        {"sender_id":1, "username":'bachdv', "list_messages":[{"message_content":"hi", "delivered_time":'2019-02-16-4T-78-09,"seen":False},...]
    """
    if len(list_incoming_messages) > 0:
        list_ids = list()

        for i in range(len(list_incoming_messages)):
            list_messages = list()
            message = dict()
            info_message = dict()
            if list_incoming_messages[i]['sender_id'] not in list_ids:
                list_ids.append(list_incoming_messages[i]['sender_id'])
                message["message_content"] = list_incoming_messages[i]['message_content'],
                message['delivered_time'] = list_incoming_messages[i]['delivered_time'],
                message["seen"] = list_incoming_messages[i]['seen']
                list_messages.append(message.copy())

                j = i + 1
                while j <= len(list_incoming_messages) - 2:
                    if list_incoming_messages[i]['sender_id'] == list_incoming_messages[j]['sender_id']:
                        message["message_content"] = list_incoming_messages[j]['message_content'],
                        message['delivered_time'] = list_incoming_messages[j]['delivered_time'],
                        message["seen"] = list_incoming_messages[j]['seen']
                        list_messages.append(message.copy())
                    j += 1

                info_message['sender_id'] = list_incoming_messages[i]['sender_id']
                info_message['username'] = list_incoming_messages[i]['username']
                info_message['list_messages'] = list_messages
                ret_incoming_messages.append(info_message.copy())

    # all messages sent
    list_messages_sent = query_db(query_message_sent, is_data_fetched=True)
    if len(list_messages_sent) > 0:
        list_ids = list()

        for i in range(len(list_messages_sent)):
            list_messages = list()
            message = dict()
            info_message = dict()
            if list_messages_sent[i]['recipient_id'] not in list_ids:
                list_ids.append(list_messages_sent[i]['recipient_id'])
                message["message_content"] = list_messages_sent[i]['message_content'],
                message['delivered_time'] = list_messages_sent[i]['delivered_time'],
                message["seen"] = list_messages_sent[i]['seen']
                list_messages.append(message.copy())

                j = i + 1
                while j <= len(list_messages_sent) - 2:
                    if list_messages_sent[i]['recipient_id'] == list_messages_sent[j]['recipient_id']:
                        message["message_content"] = list_messages_sent[j]['message_content'],
                        message['delivered_time'] = list_messages_sent[j]['delivered_time'],
                        message["seen"] = list_messages_sent[j]['seen']
                    j += 1

                info_message['recipient_id'] = list_messages_sent[i]['recipient_id']
                info_message['username'] = list_messages_sent[i]['username']
                info_message['list_messages'] = list_messages
                ret_messages_sent.append(info_message.copy())

    return ret_incoming_messages, ret_messages_sent


def show_detail_message(user_id, friend_id):

    query = "SELECT *\t" \
            "FROM\t" \
            "MESSAGE\t" \
            "WHERE (sender_id ={} and recipient_id={}) or (sender_id ={} and recipient_id ={})\tORDER BY delivered_time ASC ".format(
        user_id, friend_id,
        friend_id, user_id)

    list_data = query_db(query, is_data_fetched=True)

    if list_data and len(list_data) > 0:
        # update seen is true
        query = "UPDATE message\t" \
                "SET seen=1\t" \
                "WHERE (sender_id ={} and recipient_id={}) or (sender_id ={} and recipient_id ={})".format(user_id,
                                                                                                           friend_id,
                                                                                                           friend_id,
                                                                                                           user_id)
        query_db(query)

    return list_data


def sent_message(recipient_id, message, sender_id):

    # check table block
    if is_blocked(recipient_id, sender_id):
        print "You can not sent message, You are block by the friend"
        return 0

    if message and len(message) > 0:
        query = "INSERT INTO MESSAGE(sender_id, recipient_id, message_content)\t" \
                "VALUES\t" \
                "({},{},'{}')".format(sender_id, recipient_id, message)

        if query_db(query):
            print "Message sent successfully"
            return 1
        else:
            print "Can not sent message"
    else:
        print "Message is empty! You need enter content message"
    return 0


def count_message_unread(user_id):
    query = "SELECT COUNT (*) as message_unread\t" \
            "FROM message\t" \
            "WHERE seen =false and recipient_id={}".format(user_id)

    number_messages_unread = query_db(query, is_data_fetched=True)

    return number_messages_unread


if __name__ == '__main__':
    print show_detail_message(1, 4)
