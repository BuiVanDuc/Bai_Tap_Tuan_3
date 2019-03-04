import time

import keyboard

from friends.friend import search_friend_by_username, show_list_friends, group_friend_by_lives_in, detail_friend, \
    add_friend
from messages.message import show_list_messages, sent_message, show_detail_message
from users.user import login, register_account, search_username, block_user
from utils.checking_data_util import is_email_existed
from utils.date_util import validate_date
from utils.db_util import connect_to_sqlite
from utils.email_util import is_email_validated
from utils.password_util import validate_password, encrypt_string

if __name__ == '__main__':
    count = 0
    while True:
        try:
            if connect_to_sqlite():

                option = int(raw_input("1 --> Login | 2 --> Register:\t"))
                if option == 1:
                    username = raw_input("Username:\t")
                    password = raw_input("Password:\t")
                    user_id = login(username, password)

                    if user_id:
                        while True:
                            option = int(raw_input(" 1 --> Message | 2 --> Friend | 3 --> Logout:\t"))
                            # Message
                            if option == 1:
                                while True:
                                    option = int(raw_input("1 --> View message | 2 --> Send message | 3 --> Exit:\t"))
                                    # View message
                                    if option == 1:
                                        ret_incoming_messages, ret_messages_sent = show_list_messages(user_id)

                                        while True:
                                            option = int(
                                                raw_input(
                                                    "1 --> Incoming message | 2 --> Message sent | 3 --> Exit:\t"))
                                            # Print all incoming message
                                            if option == 1:
                                                while True:
                                                    index = 0
                                                    for incoming_message in ret_incoming_messages:
                                                        index += 1
                                                        print "{}. {}\n\tmessages:{}".format(index,
                                                                                             incoming_message[
                                                                                                 'username'],
                                                                                             incoming_message[

                                                                                                 'list_messages'])
                                                    print "Ctrl + V to view detail\n"
                                                    while True:
                                                        flag = 0
                                                        if keyboard.is_pressed('Ctrl + V'):
                                                            # Enter index in list to view detail message
                                                            index = int(raw_input('Enter index message:\t'))
                                                            friend_id = ret_incoming_messages[index - 1]['sender_id']
                                                            for message in show_detail_message(user_id, friend_id):
                                                                print message

                                                            print "Ctrl + R to reply\n"
                                                            while True:
                                                                # Ctrl + R to reply message
                                                                flag_1 = 0
                                                                if keyboard.is_pressed('Ctrl + R'):
                                                                    message_content = raw_input("Type a message:\t")
                                                                    # Enter to sent message
                                                                    sent_message(friend_id, message_content, user_id)
                                                                # Come back to --> incoming message
                                                                elif keyboard.is_pressed('Ctrl + E'):
                                                                    flag_1 = 1
                                                                    break
                                                            if flag_1 == 1:
                                                                break
                                                        # Come back to --> message
                                                        elif keyboard.is_pressed('Ctrl + B'):
                                                            print "back"
                                                            option = 0
                                                            flag = 1
                                                            break
                                                    if flag == 1:
                                                        break
                                            elif option == 2:
                                                while True:
                                                    index = 0
                                                    for message in ret_messages_sent:
                                                        index += 1
                                                        print "{}. {}\n\tmessage:{}".format(index, message["username"],
                                                                                            message['list_messages'])
                                                    print "Ctrl + V to view detail\n"
                                                    while True:
                                                        flag = 0
                                                        # Ctrl + V Detail message
                                                        if keyboard.is_pressed('Ctrl + V'):
                                                            index = int(raw_input('Enter index message:\t'))
                                                            friend_id = ret_messages_sent[index - 1]['recipient_id']
                                                            for message in show_detail_message(user_id, friend_id):
                                                                print message
                                                            print "ctrl + R to reply message"
                                                            while True:
                                                                flag_1 = 0
                                                                # Ctrl + R to reply message
                                                                if keyboard.is_pressed('Ctrl + R'):
                                                                    message_content = raw_input("Type a message:\t")
                                                                    # Enter to sent message
                                                                    sent_message(friend_id, message_content,
                                                                                 user_id)
                                                                # Back to --> message sent
                                                                elif keyboard.is_pressed('Ctrl + E'):
                                                                    flag_1 = 1
                                                                    break
                                                            if flag_1 == 1:
                                                                break
                                                        #  Back to --> message
                                                        elif keyboard.is_pressed('Ctrl + B'):
                                                            option = 0
                                                            flag = 1
                                                            break
                                                    if flag == 1:
                                                        break
                                            if option == 3:
                                                break
                                    # Sent message
                                    elif option == 2:
                                        while True:
                                            option = int(raw_input(
                                                '1 --> Enter username | 2 --> View list friend | 3 --> Exit:\t'))
                                            if option == 1:
                                                # Step1 search friend by user name:
                                                recipient = raw_input("Enter Recipient:\t")
                                                list_username = search_friend_by_username(user_id, recipient)

                                                # Step 2 print list username
                                                if len(list_username) > 0:
                                                    for i in range(len(list_username)):
                                                        print "{}. {}".format(i + 1, list_username[i]['nickname'])

                                                # Step 3 enter the corresponding number in list friend
                                                index = int(raw_input("Enter number in list friend:\t"))
                                                name_friend = list_username[index - 1]['nickname']
                                                print "To:\t{}".format(name_friend)
                                                friend_id = list_username[index - 1]['friend_id']
                                                message_content = raw_input('Type a message:\t')

                                                # Step 4 enter to sent message
                                                sent_message(friend_id, message_content, user_id)
                                            elif option == 2:
                                                list_friends = show_list_friends(user_id)

                                                # Step 1 show list friend
                                                for i in range(len(list_friends)):
                                                    print "{}. {}".format(i + 1, list_friends[i]['nickname'])

                                                # Step 2 Enter the corresponding number in list friend
                                                index = int(raw_input("Enter the corresponding number:\t"))
                                                name_friend = list_friends[index - 1]['nickname']
                                                print "To:\t{}".format(name_friend)
                                                friend_id = list_friends[index - 1]['friend_id']
                                                message_content = raw_input('Type a message:\t')

                                                # Step 3 Enter to sent message
                                                sent_message(friend_id, message_content, user_id)
                                            elif option == 3:
                                                break
                                    # Exit message
                                    elif option == 3:
                                        break
                            # Friend
                            elif option == 2:
                                while True:
                                    option = int(raw_input(
                                        "1 --> List friends | 2 --> Add fiend or Block | 3 --> Exit:"))
                                    if option == 1:
                                        # show list friend
                                        list_friends = show_list_friends(user_id)
                                        index = 0
                                        for friend in list_friends:
                                            index += 1
                                            print "{}. {}".format(index, friend['nickname'])

                                        print "Ctrl + C to group friend by City | Ctrl + B to Back | Ctrl + V view detail"
                                        # Ctrl + C to group friend
                                        while True:
                                            if keyboard.is_pressed('Ctrl + C'):
                                                groups_friend = group_friend_by_lives_in(user_id)
                                                for key, val in groups_friend.items():
                                                    print key
                                                    index = 0
                                                    count = 0
                                                    for username in val:
                                                        index += 1
                                                        print "{}. {}".format(index, username)
                                                    count += 1
                                                print "Ctrl + C to group friend by City | Ctrl + B to Back | Ctrl + V view detail"
                                            elif keyboard.is_pressed('Ctrl + V'):
                                                index = int(raw_input("Enter number in list:\t"))
                                                friend_id = list_friends[index - 1]['friend_id']
                                                list_info_friend = detail_friend(friend_id)
                                                for key, val in list_info_friend[0].items():
                                                    print key, ":", val
                                                print "Ctrl + R to reply message"
                                                while True:
                                                    if keyboard.is_pressed('Ctrl + R'):
                                                        name_friend = list_friends[index - 1]['nickname']
                                                        print "To:\t{}".format(name_friend)

                                                        friend_id = list_friends[index - 1]['friend_id']
                                                        message_content = raw_input('Type a message:\t')

                                                        sent_message(friend_id, message_content, user_id)
                                                        break
                                                print "Ctrl + C to group friend by City | Ctrl + B to Back | Ctrl + V view detail"
                                            # Back to --> Friend
                                            elif keyboard.is_pressed('Ctrl + B'):
                                                option = 0
                                                break
                                    # 2. Add fiend or Block
                                    elif option == 2:
                                        while True:
                                            name = raw_input("Enter user:\t")
                                            list_username = search_username(name)
                                            index = 0
                                            for username in list_username:
                                                index += 1
                                                print "{}. {}".format(index, username['username'])
                                            number = int(raw_input('Enter number in list:\t'))
                                            friend_id = list_username[number - 1]['id']

                                            option = raw_input(" 1 --> Add friend | 0 --> Block user")

                                            if option == 1:
                                                add_friend(friend_id, user_id)
                                            elif option == 0:
                                                block_user(user_id, friend_id)
                            # 3. Exit Friend
                            elif option == 4:
                                break
                elif option == 2:
                    email, fullname, birth_of_date, username, password, lives_in = "", "", "", "", "", ""
                    sex = 1
                    flag = 0
                    while True:
                        if is_email_validated(email):
                            if is_email_existed(email):
                                print "email account have existed. Please enter other email"
                                email = ""
                            else:
                                if len(fullname) > 0:
                                    if flag:
                                        pass
                                    else:
                                        print "(Sex) 0 -> male,1 -> female, Other"
                                        sex = int(raw_input('Sex:\t'))
                                        print "lives in can be empty"
                                        lives_in = raw_input("lives_in:\t")
                                        flag = 1
                                    if validate_date(birth_of_date):
                                        if len(username) > 0:
                                            if validate_password(password):
                                                confirm_password = raw_input("confirm_password:\t")
                                                if confirm_password == password:
                                                    password = encrypt_string(password)
                                                    if register_account(email, fullname, birth_of_date, sex, username,
                                                                        password,
                                                                        lives_in):
                                                        print "Register successfully"
                                                        break
                                                    else:
                                                        print "Can not register"
                                                        break
                                                else:
                                                    print "Password confirmation doesn't match password"
                                            else:
                                                password = raw_input("Password:\t")
                                        else:
                                            username = raw_input("Username:\t")
                                            if len(username) < 0:
                                                print " username is empty. Please enter your username"
                                    else:
                                        birth_of_date = raw_input("Date of birth:\t")
                                else:
                                    fullname = raw_input("Fullname:\t")
                                    if len(fullname) < 0:
                                        print " fullname is empty. Please enter your fullname"
                        else:
                            email = raw_input("email:\t")
                            if not is_email_validated(email):
                                print "email is invalidated. Please enter email again!!"
            else:
                print "Can not connect to DB"
                break
        except Exception as e:
            print(e)
