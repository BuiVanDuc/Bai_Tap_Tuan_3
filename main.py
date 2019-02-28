import keyboard
import time
from friends.friend import show_list_friends, search_friend_by_username, detail_friend, add_friend, \
    group_friend_by_lives_in
from messages.message import show_list_messages, sent_message, show_detail_message
from users.user import register_account, login, search_username, block_user

if __name__ == '__main__':
    while True:
        try:
            option = int(raw_input("1 --> Login | 2 --> Register:\t"))
            if option == 1:
                username = raw_input("Username:\t")
                password = raw_input("Password:\t")
                user_id = login(username, password)

                if user_id:
                    while True:
                        option = int(raw_input(" 1 --> Message | 2 --> Friend | 3 --> Logout:\t"))
                        if option == 1:
                            while True:
                                option = int(raw_input("1 --> View message | 2 --> Send message | 3 --> Exit:\t"))
                                if option == 1:
                                    ret_incoming_messages, ret_messages_sent = show_list_messages(user_id)
                                    print 'Incoming message   |   Message sent'
                                    # Print all incoming message
                                    while True:
                                        index = 0
                                        for incoming_message in ret_incoming_messages:
                                            index +=1
                                            print "{}. {}\n\tmessages:{}".format(index, incoming_message['username'], incoming_message['list_messages'])

                                        while True:
                                            flag =0
                                            print "Ctrl + V to view detail | Ctrl + N to next view"
                                            if keyboard.is_pressed('Ctrl + V'):
                                                # Enter index in list to view detail message
                                                index = int(raw_input('Enter index:\t'))
                                                friend_id = ret_incoming_messages[index - 1]['sender_id']
                                                for message in show_detail_message(user_id, friend_id):
                                                    print message
                                                while True:
                                                    # Ctrl + R to reply message
                                                    if keyboard.is_pressed('Ctrl + R'):

                                                        message_content = raw_input("Type a message:\t")
                                                        # Enter to sent message
                                                        sent_message(friend_id, message_content, user_id)
                                                        break

                                                    if keyboard.is_pressed('Ctrl + B'):
                                                        flag =1
                                            # Ctrl + N to view Messages are sent
                                            elif keyboard.is_pressed('Ctrl + N'):
                                                index = 0
                                                for message in ret_messages_sent:
                                                    index +=1
                                                    print "{}. {}".format(index, message)
                                                print "Ctrl + B to Back | Ctrl + V to view detail"

                                                while True:
                                                    # Ctrl + V Detail message
                                                    if keyboard.is_pressed('Ctrl + V'):
                                                        index = int(raw_input(
                                                            'Enter the corresponding number to view detail message:\t'))
                                                        friend_id = ret_messages_sent[index - 1]['sender_id']
                                                        for message in show_detail_message(user_id, friend_id):
                                                            print message

                                                        while True:
                                                            # Ctrl + R to reply message
                                                            if keyboard.is_pressed('Ctrl + R'):
                                                                message_content = raw_input("Type a message:\t")
                                                                # Enter to sent message
                                                                sent_message(friend_id, message_content, user_id)
                                                                break

                                                            elif keyboard.is_pressed('Ctrl + B'):
                                                                flag =1

                                            if flag:
                                                break
                                if option == 2:
                                    option = int(raw_input('1 --> Enter username: | 2 --> View list friend:\t'))
                                    if option == 1:
                                        # Step1 search friend by user name:
                                        recipient = raw_input("Enter Recipient:\t")
                                        list_username = search_friend_by_username(user_id, recipient)

                                        # Step 2 print list username
                                        if len(list_username) > 0:
                                            for i in range(len(list_username)):
                                                print "{}. {}".format(i + 1, list_username[i]['username'])

                                        # Step 3 enter the corresponding number in list friend
                                        index = int(raw_input("Enter the corresponding number:\t"))
                                        name_friend = list_username[index - 1]['username']
                                        print "To:\t{}".format(name_friend)
                                        friend_id = list_username[index - 1]['friend_id']
                                        message_content = raw_input('Type a message:\t')

                                        # Step 4 enter to sent message
                                        sent_message(friend_id, message_content, user_id)
                                    elif option == 2:
                                        print "Pressed Ctrl + L to show list friend"
                                        while True:
                                            if keyboard.is_pressed('Ctrl + L'):
                                                list_friends = show_list_messages(user_id)

                                                # Step 1 show list friend
                                                for i in range(len(list_friends)):
                                                    print "{}. {}".format(i + 1, list_friends[i]['username'])

                                                # Step 2 Enter the corresponding number in list friend
                                                index = int(raw_input("Enter the corresponding number:\t"))
                                                name_friend = list_friends[index - 1]['username']
                                                print "To:\t{}".format(name_friend)
                                                friend_id = list_friends[index - 1]['friend_id']
                                                message_content = raw_input('Type a message:\t')

                                                # Step 3 Enter to sent message
                                                sent_message(friend_id, message_content, user_id)
                        elif option == 2:
                            # show list friend
                            list_friends = show_list_friends(user_id)
                            index = 0
                            for friend in list_friends:
                                index += 1
                                print "{}. {}".format(index, friend['nickname'])

                            option = int(raw_input("1 --> To group friend by lives_in:\t"))
                            if option == 1:
                                # Ctrl + C to group friend
                                while True:
                                    if keyboard.is_pressed('Ctrl + C'):
                                        groups_friend = group_friend_by_lives_in(user_id)
                                        for key, val in groups_friend.items():
                                            print key
                                            index = 0
                                            for username in val:
                                                index += 1
                                                print "{}. {}".format(index, username)
                                        break
                            time.sleep(1)
                            while True:
                                option = int(
                                    raw_input(" 1 --> Detail friend | 2 --> Add friend | 3 --> Block | 4 --> Exit:\t"))

                                if option == 1:
                                    index = int(raw_input("Enter the corresponding number:\t"))
                                    friend_id = list_friends[index - 1]['friend_id']
                                    list_info_friend = detail_friend(friend_id)
                                    for key, val in list_info_friend[0].items():
                                        print key, ":", val
                                elif option == 2:
                                    name = raw_input("Enter user:\t")
                                    list_username = search_username(name)
                                    index = 0
                                    for username in list_username:
                                        index += 1
                                        print "{}. {}".format(index, username['username'])
                                    number = int(raw_input('Enter number in list:\t'))
                                    friend_id = list_username[number - 1]['id']
                                    add_friend(friend_id, user_id)
                                    pass
                                elif option == 3:
                                    name = raw_input("Enter user:\t")
                                    list_username = search_username(name)
                                    index = 0
                                    for username in list_username:
                                        index += 1
                                        print "{}. {}".format(index, username['username'])
                                    number = int(raw_input('Enter number in list:\t'))
                                    user_blocked_id = list_username[number - 1]['id']

                                    block_user(user_id, user_blocked_id)

                                elif option == 4:
                                    break

            elif option == 2:
                fullname = str(raw_input("Fullname:\t"))
                birth_of_date = str(raw_input("Date of birth:\t"))
                print "Sex: 0-->Male | 1 --> Female"
                sex = int(raw_input('Sex:\t'))
                username = str(raw_input("Username:\t"))
                password = str(raw_input("password:\t"))
                re_password = str(raw_input("Re_password:\t"))
                lives_in = str(raw_input("lives_in:\t"))
                register_account(fullname, birth_of_date, sex, username, password, re_password, lives_in)
        except Exception as e:
            print(e)
