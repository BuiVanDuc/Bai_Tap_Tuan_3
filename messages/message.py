from friends.functions import view_friends_by_contact_time
from functions import detail_message, sent_message, view_message
from messenger_mng.messenger_mng import display_menu
from users.functions import search_username, is_blocked, get_user_info_by_id

MENU_SEND = '''MANAGER SENT MESSAGE
1. Enter Name
2. View list friends
3. Back to Message
'''


def display_message_send():
    try:
        print MENU_SEND
        option = raw_input("Choose your option: ")
        return int(option)
    except Exception as ex:
        print ex
        return -1


def display_view_detail_message(user_id, username):
    ret_data = view_message(user_id, username)

    index = 0
    if ret_data and len(ret_data) > 0:
        index += 1
        for item in ret_data:
            print "{}. {}\n\tmessages:{}".format(index, item['username'], item['list_messages'])
    else:
        print 'Have no message'
        return -1

    try:
        print '''MANAGER DETAIL MESSAGES
                0: Exit
                Other number(in list): view detail a message
              '''

        number = int(raw_input("Choose your option:\t"))
        if number == 0:
            print "Exit"
        elif 0 < number <= len(ret_data):
            index = number - 1
            friend_id = ret_data[index]['recipient_id']
            print detail_message(user_id, friend_id)
            return friend_id
        else:
            print "invalid option !!!"
            return -1
    except Exception as ex:
        print(ex)
        return -1


def display_reply_message(user_id, friend_id):
    try:
        print '''MANAGER REPLY MESSAGE
                0: Exit
                1: Reply
             '''
        number = int(raw_input('Choose your option:\t'))
        if number == 0:
            print "Exit"
            return -1
        elif number == 1:
            if is_blocked(user_id, friend_id) == 1:
                print "Please Unblocked to sent message!!"
                return -1
            elif is_blocked(user_id, friend_id) == 2:
                print "You are blocked, can not sent message!!"
                return -1
            else:
                message_content = raw_input("Type a message:\t")
                if message_content and len(message_content) > 0:
                    if sent_message(friend_id, message_content, user_id):
                        print "Sent message successfully"
                    else:
                        print "Can not sent message"
                        return -1
                else:
                    print "Message is empty, please try again"
                    return -1
        else:
            print "invalid option, please choose:0 or 1"
            return -1
    except Exception as Ex:
        print(Ex)
        return -1


def display_send_message_by_search_username(user_id):
    try:
        username = raw_input("Search:\t")
        if username and len(username) > 0:
            list_username = search_username(username)

            if list_username and len(list_username) > 0:
                index = 0
                for username in list_username:
                    index += 1
                    print "{}. {}".format(index, username['username'])

                print "Choose number (in list) sent message"
                number = int(raw_input("number:\t"))

                if 0 < number <= len(list_username):
                    index = number - 1
                    recipient_id = list_username[index]['id']
                    if is_blocked(user_id, recipient_id):
                        print "Please unblock to sent message!!"
                        return -1
                    elif is_blocked(user_id, recipient_id) == 2:
                        print "Can not sent message. You are blocked!!"
                    else:
                        message_content = raw_input("Type a message:\t")

                        if message_content and len(message_content) > 0:
                            if sent_message(recipient_id, message_content, user_id):
                                print "Sent message successfully"
                            else:
                                print "Can not sent message !!"
                                return -1
                        else:
                            print "Message content is empty, please try again"
                            return -1
                elif number ==0:
                    print "Back to message"
                else:
                    print "Invalid option, please try again"
            else:
                print "No result"
                return -1
        else:
            print "Username is empty, please try again!!"
            return -1
    except Exception as Ex:
        print (Ex)
        return -1


def display_sent_message_by_list_friend(user_id):
    try:
        list_friends = view_friends_by_contact_time(user_id)

        if list_friends and len(list_friends) > 0:
            index = 0
            for friend in list_friends:
                index += 1
                print "{}. {}".format(index, friend['nickname'])

            print "Choose number (in list) sent message"
            number = int(raw_input("number:\t"))

            if 0 < number <= len(list_friends):
                index = number - 1
                recipient_id = list_friends[index]['friend_id']

                # Check block
                if is_blocked(user_id, recipient_id) == 1:
                    print "Please Unblock to sent message"
                    return -1
                elif is_blocked(user_id, recipient_id) == 2:
                    print "Can not sent message. You are blocked!!"
                    return -1
                else:
                    message_content = raw_input("Type a message:\t")

                    if message_content and len(message_content) > 0:
                        if sent_message(recipient_id, message_content, user_id):
                            print "Sent message successfully!!"
                        else:
                            print "Can not sent message"
                            return -1
                    else:
                        print "Message content is empty, please try again"
                        return -1
            else:
                print "option invalid, please try again!!"
                return -1
        else:
            print "No have friend"
            return -1
    except Exception as Ex:
        print Ex
        return -1


def display_message(user_id):
    username = get_user_info_by_id(user_id)['username']
    messages = view_message(user_id, username)

    if messages and len(messages) > 0:
        index = 0
        for message in messages:
            index += 1
            if 'unread' in message:
                print "{}. {} - unread:{}".format(index, message['username'], message['unread'])
            else:
                print "{}. {}".format(index, message['username'])

        print ''' 
                    0: Exit
                    Other number(in list message): view detail a message
        '''
        try:
            number = int(raw_input('Number:\t'))
            if number == 0:
                print "Exit"
                return -1
            elif 0 < number <= len(messages):
                index = number - 1
                friend_id = messages[index]['id']
                friend_name = messages[index]['username']
                list_data = detail_message(user_id, friend_id)

                for data in list_data:
                    if data['sender_id'] == user_id:
                        print "{}: {} - {}".format('me', data['message_content'], data['delivered_time'])
                    elif data['recipient_id'] == user_id:
                        print "\t{}: {} - {}".format(friend_name, data['message_content'], data['delivered_time'])
                return friend_id
            else:
                print "Invalid number, please try again!!"
                return -1
        except Exception as Ex:
            print (Ex)
            return -1
    else:
        print "No message"
        return -1


def messages(user_id):
    while True:
        option = display_menu(2)
        if option == 1:
            '''
                View
            '''
            while True:
                print "*****Chats*****"
                friend_id = display_message(user_id)
                if friend_id != -1:
                    display_reply_message(user_id, friend_id)
                else:
                    break
        elif option == 2:
            '''
                Send message
            '''
            while True:
                option = display_message_send()
                if option == 1:
                    display_send_message_by_search_username(user_id)
                elif option == 2:
                    display_sent_message_by_list_friend(user_id)
                elif option == 3:
                    print "Back to message"
                    break
                else:
                    print "invalid option, choose options: 1,2 or 3"
                    return -1
        elif option == 3:
            print 'Back to main'
            break